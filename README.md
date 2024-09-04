# Image-Processing
A Python script that performs local histogram equalization on grayscale images to enhance contrast using a neighborhood window. This technique improves local contrast and can be useful for various image processing applications.

#Local Histogram Equalization

This repository contains a Python script for performing local histogram equalization on grayscale images. Local histogram equalization enhances contrast by equalizing the histogram of a pixel's neighborhood rather than the entire image, which can improve local contrast and detail.

## Features

- **Local Histogram Equalization:** Enhances local contrast by applying histogram equalization within a neighborhood window.
- **Neighborhood Size:** Customizable size of the neighborhood window (e.g., 3x3, 5x5).
- **Grayscale Image Processing:** Supports 8-bit grayscale images.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Matplotlib

You can install the required packages using pip:

```bash
pip install opencv-python numpy matplotlib
