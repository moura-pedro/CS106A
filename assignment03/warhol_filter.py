"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    # Generates recolored image from path image
    image = make_recolored_patch(rand(), rand(), rand())

    # Takes height and width from the the new recolored image
    height = image.height
    width = image.width

    # Create a blank image
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    for rows in range(N_ROWS):
        for columns in range(N_COLS):
            for y in range(height):
                for x in range(width):
                    # Get pixels from 'image'.
                    pixel = image.get_pixel(x, y)
                    # Set pixels from 'image', at 'final_image'
                    final_image.set_pixel(x + (PATCH_SIZE * columns), y + (PATCH_SIZE * rows), pixel)
            # Generates a new recolored image.
            image = make_recolored_patch(rand(), rand(), rand())

    # Show all images generated at the blank image created before
    final_image.show()


def rand():
    # Generates random numbers from 0 - 1.5
    random_value = random.uniform(0, 1.5)
    return random_value


def make_recolored_patch(red_scale, green_scale, blue_scale):
    # Return a recolored patch by setting new pixels values
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch


if __name__ == '__main__':
    main()
