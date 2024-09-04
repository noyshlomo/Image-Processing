import cv2
import numpy as np
import matplotlib.pyplot as plt

def local_histogram_equalization(image, neighborhood_size=3, L=256):
    """
    Perform local histogram equalization on an image using a neighborhood window.
    
    Parameters:
        image (numpy.ndarray): The input grayscale image.
        neighborhood_size (int): The size of the neighborhood window (e.g., 3 for a 3x3 neighborhood).
        L (int): Number of intensity levels in the image (default is 256 for 8-bit images).
    
    Returns:
        numpy.ndarray: The locally equalized image.
    """
    h, w = image.shape # Get the height (h) and width (w) of the image.
    enhanced_image = np.zeros_like(image) # Empty image to store the results of the local histogram equalization.

    # Pad the image to handle borders
    pad_size = neighborhood_size // 2
    padded_image = np.pad(image, pad_size, mode='reflect')

    # Iterate over each pixel in the original image
    for i in range(h):
        for j in range(w):
            # Extract the neighborhood around the current pixel
            neighborhood = padded_image[i:i+neighborhood_size, j:j+neighborhood_size]

            # Compute the histogram of the neighborhood
            hist, _ = np.histogram(neighborhood, bins=L, range=(0, L))

            # Compute the cumulative distribution function (CDF)
            cdf = hist.cumsum()
            cdf_normalized = cdf * (L - 1) / cdf[-1]  # Normalize the CDF

            # Get the intensity value of the current pixel
            current_value = image[i, j]

            # Equalize the current pixel using the CDF
            enhanced_image[i, j] = cdf_normalized[current_value]

    return enhanced_image

# Load the image
image_path = 'embedded_squares.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error loading image. Please check the path.")
else:
    # Apply the local histogram equalization
    neighborhood_size = 3  # Neighborhood size is 3x3
    enhanced_image = local_histogram_equalization(image, neighborhood_size, L=256)

    # Plotting the original and enhanced images
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(image, cmap='gray', vmin=0, vmax=255)
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    axes[1].imshow(enhanced_image, cmap='gray', vmin=0, vmax=255)
    axes[1].set_title('Locall Histogram Equalization')
    axes[1].axis('off')

    plt.show()

    # Save the locally enhanced image (optional)
    # cv2.imwrite('enhanced_image.jpg', enhanced_image)
