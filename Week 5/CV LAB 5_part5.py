import cv2
import numpy as np
from datetime import datetime

# Desired frame width and height
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Load the reference image
reference_img = cv2.imread('/home/upasana/Desktop/CV/atom.jpg', 0)

# For video recording
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None  # VideoWriter object
recording = False

if reference_img is None:
    print("Failed to load the reference image")
    exit()

# Initialize the SIFT detector
sift = cv2.SIFT_create()

# Compute keypoints and descriptors for the reference image
kp1, des1 = sift.detectAndCompute(reference_img, None)

# Initialize the Brute-Force Matcher
bf = cv2.BFMatcher()

def filter_matches(matches):
    good_matches = []
    for m, n in matches:
        if m.distance < 0.6 * n.distance:
            good_matches.append(m)
    return good_matches

# Start the webcam capture
cap = cv2.VideoCapture(0)

# Set the desired frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    kp2, des2 = sift.detectAndCompute(gray_frame, None)
    
    matches = bf.knnMatch(des1, des2, k=2)
    good_matches = filter_matches(matches)
    
    img_matches = cv2.drawMatches(reference_img, kp1, gray_frame, kp2, good_matches, None)
    
    cv2.imshow("Matches", img_matches)
    
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break
    elif key == ord('c'):
        cv2.imshow('Matches', np.ones_like(frame) * 255)
        cv2.waitKey(100)
        
        dt_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        img_name_name = f"captured_{dt_string}.jpg".replace(":", "_")
        cv2.imwrite(img_name_name, frame)
        print(f"Image saved as {img_name_name}")
    elif key == ord('v'):
        if recording:
            out.release()
            print("Recording stopped.")
            recording = False
        else:
            dt_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            video_name = f"recorded_{dt_string}.avi".replace(":", "_")
            out = cv2.VideoWriter(video_name, fourcc, 20.0, (FRAME_WIDTH, FRAME_HEIGHT))
            print(f"Recording started. Saving to {video_name}")
            recording = True

    if recording:
        out.write(frame)

cap.release()
if recording:
    out.release()
cv2.destroyAllWindows()
