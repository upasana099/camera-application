# Webcam Zoom and Recording

This Python script uses the OpenCV library to capture video from a webcam, allowing the user to zoom in on the live feed using a trackbar. Additionally, the script provides the functionality to capture images ('c' key) and start/stop video recording ('v' key).

## Prerequisites

- Python 3.x
- OpenCV (`pip install opencv-python`)

## Usage

1. Run the script.
2. Adjust the zoom level using the trackbar.
3. Press 'c' to capture a still image.
4. Press 'v' to start/stop video recording.
5. Press 'Esc' to exit the program.

## Trackbar

The trackbar labeled 'Zoom' controls the zoom factor of the webcam feed. A value of 1 corresponds to no zoom, and higher values indicate zoomed-in views.

## Image Capture

Pressing the 'c' key captures a still image from the webcam feed. The image is saved in the current directory with a filename indicating the capture time.

## Video Recording

Pressing the 'v' key toggles video recording. When recording is started, a video file is created in the current directory with a filename indicating the start time. Subsequent presses of 'v' stop the recording.

## Dependencies

- OpenCV: 4.x

## File Output

- Captured images are saved in the current directory with filenames in the format: `captured_<timestamp>.jpg`.
- Recorded videos are saved in the current directory with filenames in the format: `recorded_<timestamp>.avi`.


