# Object Recognition with SIFT Matching

This Python script uses the SIFT (Scale-Invariant Feature Transform) algorithm and Brute-Force matching to detect and match features between a reference image and the live webcam feed. The script provides options for capturing images and recording videos when specific keys are pressed.

## Prerequisites

- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)

## Usage

1. Run the script.
2. The live webcam feed will display with feature matches between the reference image and the current frame.
3. Press 'c' to capture an image. The image will be saved with a timestamp.
4. Press 'v' to start or stop recording a video. The video will be saved with a timestamp.
5. Press 'q' or 'Esc' to exit the program.

## Features

- SIFT feature detection and matching.
- Capture images with timestamped filenames.
- Record videos with timestamped filenames.

## Configuration

- **FRAME_WIDTH:** Desired width of the webcam frame.
- **FRAME_HEIGHT:** Desired height of the webcam frame.

## Dependencies

- OpenCV: 4.x
- NumPy: Latest

