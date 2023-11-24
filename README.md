# Camera Application -OpenCV

A collection of Python scripts for various computer vision tasks using the OpenCV library.

## 1. Feature: Zoom and Capture

### Description

This script utilizes OpenCV to interact with the webcam, providing functionalities such as zooming the camera feed and capturing images with a timestamp. It also supports video recording with start and stop options.

### Usage

1. Run the script.
2. Use the trackbar to adjust zoom levels.
3. Press 'c' to capture an image with a timestamp.
4. Press 'v' to start or stop recording a video with a timestamp.
5. Press 'Esc' to exit the program.



---

## 2. Image Processing

### Description

This script demonstrates various image processing techniques applied to the live webcam feed. It includes options for custom Sobel and Laplacian filters, Gaussian blur, and skin thresholding.

### Usage

1. Run the script.
2. Use different keys to apply specific image processing techniques.
3. Press 's' to toggle Sobel X filter.
4. Press 'd' to toggle Canny edge detection.
5. Press '4' to toggle the display of multiple processed windows.

### Dependencies

- OpenCV: 4.x
- NumPy: Latest


---

## 3. Logo Overlay and Edge Detetection

### Description

This script overlays the OpenCV logo onto the live webcam feed. It includes a dynamic timestamp and a constant red border around the frame.

### Usage

1. Run the script.
2. The OpenCV logo will be blended with the webcam feed.
3. Press 's' to toggle Sobel X filter.
4. Press 'd' to toggle Canny edge detection.
5. Press '4' to toggle the display of multiple processed windows.

### Dependencies

- OpenCV: 4.x
- NumPy: Latest


---

## 4. SIFT Object Recognition

### Description

This script utilizes the SIFT algorithm for object recognition in live webcam feed. It matches features between a reference image and the current frame and provides options for capturing images and recording videos.

### Usage

1. Run the script.
2. Features between the reference image and webcam feed will be displayed.
3. Press 'c' to capture an image with a timestamp.
4. Press 'v' to start or stop recording a video with a timestamp.
5. Press 'q' or 'Esc' to exit the program.

### Dependencies

- OpenCV: 4.x



