# Hand Gesture Recognition with Emoji Display

### Overview
This Python script uses the MediaPipe library for hand tracking and OpenCV to capture video frames from a webcam. It recognizes hand gestures such as thumbs up, thumbs down, one thumbs up, and one thumbs down. Additionally, it displays corresponding emoji images on the screen based on detected gestures.

## Requirements
- Python 3.x
- OpenCV
- NumPy
- MediaPipe

Install the required Python libraries using the following:
```bash
pip install opencv-python numpy mediapipe
```
## Usage

1. Clone the repository or download the script `hand_gesture_recognition.py`.

2. Download emoji images for thumbs up and thumbs down. Update the paths to the emoji images in the script:

    ```python
    thumbs_up_emoji_path = '/path/to/thumbs_up.png'
    thumbs_down_emoji_path = '/path/to/thumbs_down.png'
    ```

3. Run the script:

    ```bash
    python hand_gesture_recognition.py
    ```

4. A window will open displaying the webcam feed. The script will recognize hand gestures and display corresponding emoji images on the screen.

5. Press 'ESC' to exit the application.

## Customization

- Adjust the paths to emoji images based on your local directory structure.

## Notes

- Ensure that your webcam is properly connected and accessible.
- The script uses gestures such as two thumbs up, two thumbs down, one thumbs up, and one thumbs down.

Feel free to adapt and modify the script according to your specific use case!
