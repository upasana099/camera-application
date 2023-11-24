# Webcam Features with OpenCV

This Python script utilizes OpenCV to interact with a webcam, providing various features such as zooming, image capture, video recording, and image processing.

## Prerequisites

- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- Matplotlib (`pip install matplotlib`)

## Usage

1. Run the script.
2. Adjust the zoom level using the 'Zoom' trackbar.
3. Press 'c' to capture a still image.
4. Press 'e' to extract yellow color from the frame.
5. Press 'r' to rotate the frame by 10 degrees.
6. Press 't' to apply a skin tone threshold.
7. Press 'b' to apply Gaussian blur with customizable parameters.
8. Press 's' to apply a sharpening filter.
9. Press 'Esc' to exit the program.

## Trackbars

- **Zoom:** Controls the zoom factor of the webcam feed.
- **Sigma X:** Controls the horizontal standard deviation for Gaussian blur.
- **Sigma Y:** Controls the vertical standard deviation for Gaussian blur.

## Image Capture

Pressing the 'c' key captures a still image from the webcam feed. The image is saved in the current directory with a filename indicating the capture time.

## Yellow Color Extraction

Pressing the 'e' key extracts yellow color from the frame and displays the original frame, the mask, and the result.

## Rotation

Pressing the 'r' key rotates the frame by 10 degrees.

## Skin Tone Thresholding

Pressing the 't' key applies a skin tone threshold to the frame, highlighting areas with skin tones.

## Gaussian Blur

Pressing the 'b' key applies Gaussian blur to the frame. Adjust the 'Sigma X' and 'Sigma Y' trackbars for custom blurring.

## Sharpening

Pressing the 's' key applies a sharpening filter to the frame.

## Video Recording

- Press 'v' to start/stop video recording. Recorded videos are saved in the current directory with filenames in the format: `recorded_<timestamp>.avi`.

## Dependencies

- OpenCV: 4.x
- NumPy: Latest
- Matplotlib: Latest
