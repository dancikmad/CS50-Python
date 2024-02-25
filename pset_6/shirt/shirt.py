# -*- coding: utf-8 -*-
from PIL import Image, ImageOps
import sys
import os.path

def overlay_images(input_path, output_path):

    try:
        # Open the input image
        input_image = Image.open(input_path)

        # Open the overlay image
        shirt = Image.open("shirt.png")

        # Get the size of the input image
        shirt_size = shirt.size

        # Resize and crop the input image
        resized_input = ImageOps.fit(input_image, shirt_size)

        # Overlay the overlay image on the input image
        resized_input.paste(shirt, (0, 0), shirt)

        # Save the result as the output image
        resized_input.save(output_path)

    except FileNotFoundError:
        sys.exit("Input does not exist.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            exit("Too few command-line arguments")
        else:
            exit("Too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]


    # Check for valid extensions for input and output files [".jpeg", ".jpeg", ".png"]
    # Define a tupple that stores valid extensions
    valid_extensions = (".jpeg", ".jpg", ".png")

    if not (input_path.lower().endswith(valid_extensions) and output_path.lower().endswith(valid_extensions)):
        sys.exit("Invalid output")

    if os.path.splitext(input_path.lower())[-1] != os.path.splitext(output_path.lower())[-1]:
        sys.exit("Input and output have different extensions")


    overlay_images(input_path, output_path)

