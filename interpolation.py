import numpy as np
import cv2
from PIL import Image

# Open an image file
image = Image.open("path/to/your/image_1.jpg")



def resize_image_quadratic_spline(img, new_width, new_height):
    # Get the dimensions of the input image
    height, width = img.shape[:2]

    # Create an output image with the desired size
    output = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Calculate the scaling ratios
    ratio_x = float(width) / new_width
    ratio_y = float(height) / new_height

    # Perform quadratic spline interpolation for image resizing
    for y in range(new_height):
        for x in range(new_width):
            for c in range(3):  # Iterate over color channels (assuming RGB image)
                # Calculate the corresponding coordinates in the original image
                original_x = x * ratio_x
                original_y = y * ratio_y

                # Find the nearest integer indices and fractional parts
                x0 = int(original_x)
                y0 = int(original_y)
                dx = original_x - x0
                dy = original_y - y0

                # Perform quadratic spline interpolation
                p00 = img[max(0, y0 - 1), max(0, x0 - 1), c]
                p01 = img[max(0, y0 - 1), min(width - 1, x0), c]
                p02 = img[max(0, y0 - 1), min(width - 1, x0 + 1), c]
                p10 = img[min(height - 1, y0), max(0, x0 - 1), c]
                p11 = img[y0, x0, c]
                p12 = img[min(height - 1, y0), min(width - 1, x0 + 1), c]
                p20 = img[min(height - 1, y0 + 1), max(0, x0 - 1), c]
                p21 = img[min(height - 1, y0 + 1), x0, c]
                p22 = img[min(height - 1, y0 + 1), min(width - 1, x0 + 1), c]

                # Interpolate along the x-axis
                fx1 = p11 + (p12 - p11) * dx
                fx2 = p21 + (p22 - p21) * dx

                # Interpolate along the y-axis
                fy = fx1 + (fx2 - fx1) * dy

                # Set the interpolated pixel values in the output image
                output[y, x, c] = fy

    return output


# Define the desired width and height for resizing
new_width = int(input("Enter the desired width: "))
new_height = int(input("Enter the desired height: "))
image_number = int(input("Enter the image number: "))
# Load the input image
# we have to change the path to the image by increment of 1
image_path = "input_image_" + str(image_number) + ".jpg"
image = cv2.imread(image_path)


# Resize the image using quadratic spline interpolation
resized_image = resize_image_quadratic_spline(image, new_width, new_height)

# Display the resized image
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
