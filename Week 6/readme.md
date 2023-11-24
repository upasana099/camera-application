# Image Stitching with OpenCV

## Overview

This Python script uses OpenCV to capture images from a webcam and performs image stitching to create a panorama. It employs the Scale-Invariant Feature Transform (SIFT) algorithm for keypoint detection and matching.

## Features

- **Webcam Capture:** The script captures images from a webcam.
- **Key Point Detection:** Utilizes the SIFT algorithm to detect keypoints in the captured images.
- **Matching:** Matches keypoints between successive images.
- **Stitching:** Combines the matched images to create a panorama.

## Usage

1. **Run the Script:** Execute the script in a Python environment.
2. **Capture Images:** Press 'p' to capture images from the webcam. The script captures a maximum of 5 images.
3. **View Process:** After capturing images, the script displays keypoints, matches, and the stitched panorama.
4. **Exit:** Press the 'Esc' key to exit the script.
