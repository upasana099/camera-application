import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Function to check for one thumbs up and return True if detected
def is_thumbs_up(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

    # Check if thumb is above the index finger (in the image's coordinate system)
    return thumb_tip.y < index_finger_tip.y

# Function to check for two thumbs up and return True if detected
def are_two_thumbs_up(results):
    # Initialize counters for thumbs up
    thumbs_up_count = 0

    # Iterate through all detected hands
    for hand_landmarks in results.multi_hand_landmarks:
        # Check if the current hand is showing thumbs up
        if is_thumbs_up(hand_landmarks):
            thumbs_up_count += 1

    # Return True if two thumbs up are detected
    return thumbs_up_count >= 2

# Function to check for one thumbs down and return True if detected
def is_thumbs_down(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

    # Check if thumb is below the index finger (in the image's coordinate system)
    return thumb_tip.y > index_finger_tip.y

# Function to check for two thumbs down and return True if detected
def are_two_thumbs_down(results):
    # Initialize counters for thumbs down
    thumbs_down_count = 0

    # Iterate through all detected hands
    for hand_landmarks in results.multi_hand_landmarks:
        # Check if the current hand is showing thumbs down
        if is_thumbs_down(hand_landmarks):
            thumbs_down_count += 1

    # Return True if two thumbs down are detected
    return thumbs_down_count >= 2

# Function to display emoji based on gesture
def display_emoji(image, emoji_path, x, y, hand_landmarks, gesture_text):
    emoji = cv2.imread(emoji_path, cv2.IMREAD_UNCHANGED)
    emoji = cv2.resize(emoji, (100, 100))  # Adjust the size as needed

    # Iterate through all detected hands
    for hand_landmarks in results.multi_hand_landmarks:
        # Get the coordinates for the region of interest (ROI)
        thumb_tip = (int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image.shape[1]),
                     int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image.shape[0]))

        # Define the ROI based on the size of the emoji
        roi = image[thumb_tip[1]:thumb_tip[1] + emoji.shape[0], thumb_tip[0]:thumb_tip[0] + emoji.shape[1]]

        # Check if the image has an alpha channel
        if emoji.shape[2] == 4:
            alpha_channel = emoji[:, :, 3] / 255.0
            alpha_channel = cv2.resize(alpha_channel, (roi.shape[1], roi.shape[0]))  # Resize alpha channel to match ROI size
            alpha_channel_colored = np.stack([alpha_channel] * 3, axis=2)
            blended = (alpha_channel_colored * emoji[:, :, :3] + (1 - alpha_channel_colored) * roi).astype(np.uint8)
        else:
            # If the image has only three channels, directly use it for blending (no alpha channel)
            blended = roi

        # Place the blended ROI back into the frame
        image[thumb_tip[1]:thumb_tip[1] + emoji.shape[0], thumb_tip[0]:thumb_tip[0] + emoji.shape[1]] = blended

    # Apply tint to the entire background for two thumbs-up and two thumbs-down gestures
    alpha = 0.5  # Adjust the alpha value for the desired transparency
    if "Two Thumbs Up" in gesture_text:
        tint_color = (0, 255, 0)  # Green tint for background
    elif "Two Thumbs Down" in gesture_text:
        tint_color = (0, 0, 255)  # Red tint for background
    else:
        return  # No tint for other gestures

    image[:, :] = ((1 - alpha) * image[:, :] + alpha * np.array(tint_color)).astype(np.uint8)

# Paths to emoji images
thumbs_up_emoji_path = '/home/upasana/Desktop/CV/thumbs_up.png'
thumbs_down_emoji_path = '/home/upasana/Desktop/CV/thumbs_down.png'

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)

    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and get the hand landmarks
    results = hands.process(image_rgb)

    # Draw the hand annotations on the image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Check for gestures and display the corresponding emoji on the screen
        if are_two_thumbs_up(results):
            gesture_text = "Two Thumbs Up"
            display_emoji(image, thumbs_up_emoji_path, 50, 50, hand_landmarks, gesture_text)
        elif are_two_thumbs_down(results):
            gesture_text = "Two Thumbs Down"
            display_emoji(image, thumbs_down_emoji_path, 50, 50, hand_landmarks, gesture_text)
        elif is_thumbs_up(hand_landmarks):
            gesture_text = "Thumbs Up"
            display_emoji(image, thumbs_up_emoji_path, 50, 50, hand_landmarks, gesture_text)
        elif is_thumbs_down(hand_landmarks):
            gesture_text = "Thumbs Down"
            display_emoji(image, thumbs_down_emoji_path, 50, 50, hand_landmarks, gesture_text)
        else:
            gesture_text = "Unknown Gesture"

        # Display the gesture text on the screen
        cv2.putText(image, gesture_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # Display the image
    cv2.imshow('CV Final Project', image)

    if cv2.waitKey(5) & 0xFF == 27:  # Exit on pressing 'ESC'
        break

cap.release()
cv2.destroyAllWindows()
