# Camera Image Processing with OpenCV

This Python script utilizes OpenCV to interact with a webcam, providing various image processing features such as zooming, custom Sobel operators, custom Laplacian filter, and Canny edge detection. The script also incorporates OpenCV logo blending on the webcam feed.

## Prerequisites

- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- Matplotlib (`pip install matplotlib`)

## Usage

1. Run the script.
2. Adjust the image processing options using the specified key commands.
3. Press 'Esc' to exit the program.

## Image Processing Options

### Zooming

- Press 's' to enable image processing mode.
- Press 'x' to apply Sobel X operator.
- Press 'y' to apply Sobel Y operator.
- Press 'd' to apply Canny edge detection.

### Additional Options

- Press '4' to toggle the display of additional windows showing custom Sobel and Laplacian results.

### OpenCV Logo

The OpenCV logo is blended onto the webcam feed, providing a visual representation of the image processing.

## Trackbars

- **Kernel Size:** Controls the kernel size for Sobel X and Y operators.
- **Threshold 1:** Controls the first threshold for Canny edge detection.
- **Threshold 2:** Controls the second threshold for Canny edge detection.

## Dependencies

- OpenCV: 4.x
- NumPy: Latest
- Matplotlib: Latest
