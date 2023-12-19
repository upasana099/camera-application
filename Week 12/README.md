# Flower Classification with Webcam using TensorFlow and OpenCV

## Overview
This Python script utilizes a pre-trained TensorFlow model for flower classification and uses OpenCV to capture video frames from a webcam, making real-time predictions about the flower in the frame.

## Requirements
- Python 3.x
- TensorFlow
- OpenCV
- Numpy

Install the required Python libraries using the following:
```bash
pip install opencv-python tensorflow numpy
```


## Usage
1. Clone the repository or download the script `flower_classification_webcam.py`.

2. Make sure you have a trained model saved in the TensorFlow SavedModel format or an h5 file. Update the model path in the script:
   ```python
   model = tf.keras.models.load_model('/path/to/your/flower_classification_model.h5')
   ```
3. Run the script:

  ```python
  python flower_classification_webcam.py
   ```

4. A window will open displaying the webcam feed, and the script will make predictions about the flowers in real-time. The predicted class label and the prediction score will be overlaid on the video feed.

5. Press 'q' to exit the application.


## Customization
- Adjust the size of the input image based on your model input size:
   ```python
   img = cv2.resize(frame, (180, 180))  # Adjust the size based on your model input size
   ```
- Customize the class labels based on your trained model:
   ```python
   class_labels = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
   ```

## Notes
- Ensure that your webcam is properly connected and accessible.
- The script assumes a model that expects input images in the range [0, 1]. If your model uses a different input range, adjust the normalization accordingly.

Feel free to adapt and modify the script according to your specific use case!
```
