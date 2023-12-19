import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('/home/upasana/Desktop/CV/flower_classification_model.h5')

# Open the webcam
cap = cv2.VideoCapture(0)

# Custom labels for your classes
class_labels = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Preprocess the image for model prediction
    img = cv2.resize(frame, (180, 180))  # Adjust the size based on your model input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Rescale to match the training data preprocessing

    # Make predictions
    predictions = model.predict(img_array)

    # Get the predicted class index and label
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]

    # Get the prediction score
    prediction_score = predictions[0][predicted_class_index]

    # Display the predicted class label and prediction score on the frame with black text
    text = f"Prediction: {predicted_class_label} ({prediction_score:.2f})"
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('Flower Classification', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
