# creates a mask using the original png and sets a particular image to the background of the png
# run time sucks
# https://medium.com/fnplus/blue-or-green-screen-effect-with-open-cv-chroma-keying-94d4a6ab2743
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
def png_background(path):
    image = cv2.imread(path)

    # Convert the image to RGB color space
    image_copy = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the color range for black (in this case, [0, 0, 0])
    black = np.array([0, 0, 0], dtype=np.uint8)

    # Create a boolean mask where True indicates the pixels that are black
    mask = np.all(image_copy == black, axis=2)

    # Set all black values in image_copy to 0
    image_copy[mask] = [0, 0, 0]

    background_image = cv2.imread('./background/img1.png')
    background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

    crop_background = background_image[0:720, 0:960]

    # Resize image_copy to match the shape of crop_background
    image_copy = cv2.resize(image_copy, (crop_background.shape[1], crop_background.shape[0]))

    # Use image_copy as a mask to set all non-black pixels in crop_background to black
    crop_background[np.all(image_copy != [0, 0, 0], axis=2)] = [0, 0, 0]

    final_image = crop_background + image_copy
    # Save the final image as a JPEG using plt.savefig()
    plt.imsave(path, final_image)
