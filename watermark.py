#!/usr/bin/env python

import argparse
import cv2
import os
from imwatermark import WatermarkEncoder, WatermarkDecoder

# This variable determines what AI to watermark for
watermark_type = "SDV2"  # In this case, Stable Diffusion v2.0

def decode(file, decoder):
    print(f":: Decoding {file}")

    image_file = cv2.imread(file)
    watermark = decoder.decode(image_file, "dwtDct")
    mark = watermark.decode("utf-8")
    print(f":: {file} - watermark: {mark}, {watermark}")

def encode(file, encoder):
    print(f":: Encoding {file}")

    encoder.set_watermark("bytes", watermark_type.encode("utf-8"))

    # Split the file name and extension
    file_name, file_extension = os.path.splitext(file)

    image_file = cv2.imread(file)
    image_file_encoded = encoder.encode(image_file, "dwtDct")
    cv2.imwrite(f"{file_name}-watermarked{file_extension}", image_file_encoded)

if __name__ == "__main__":
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("--encode", action="store_true")
    argumentParser.add_argument("--decode", action="store_true")
    argumentParser.add_argument("--directory", type=str)
    arguments = argumentParser.parse_args()

    amount_encoded: int = 0
    amount_decoded: int = 0

    if arguments.encode:
        encoder = WatermarkEncoder()
    if arguments.decode:
        decoder = WatermarkDecoder("bytes", 32)

    for file in os.listdir(arguments.directory):
        # Check if file exists
        if os.path.isfile(file):
            # Check the file extension
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                if arguments.encode:
                    encode(file, encoder)
                    amount_encoded += 1 
                if arguments.decode:
                    decode(file, decoder)
                    amount_decoded += 1

    # To do: Reduce code duplication

    # Print without a newline
    print(f":: Encoded {amount_encoded} image", end='')
    if amount_decoded != 1:
        print("s") # Add an 's' to the word 'image'
    elif amount_decoded == 1:
        print() # Only print a newline character
    
    # Print without a newline
    print(f":: Decoded {amount_decoded} image", end='')
    if amount_decoded != 1:
        print("s") # Add an 's' to the word 'image'
    elif amount_decoded == 1:
        print() # Only print a newline character