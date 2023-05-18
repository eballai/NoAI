#!/usr/bin/env python
import argparse
import cv2
import os
import sys
from imwatermark import WatermarkEncoder, WatermarkDecoder
from colorama import Fore
from decode import decode
from encode import encode

def main():
    # This variable determines what AI to watermark for
    watermark_type = "SDV2"  # In this case, Stable Diffusion v2.0

    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("--encode", action="store_true")
    argumentParser.add_argument("--decode", action="store_true")
    argumentParser.add_argument("--directory", type=str)
    arguments = argumentParser.parse_args()

    if not len(sys.argv) > 1:
        print(f":: {Fore.RED}Error{Fore.RESET}: No arguments have been provided!")
        argumentParser.print_help()
        sys.exit(1)

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
                    encode(file, encoder, watermark_type)
                    amount_encoded += 1 
                if arguments.decode:
                    decode(file, decoder, watermark_type)
                    amount_decoded += 1

    # To do: Reduce code duplication

    if arguments.encode:
        # Print without a newline
        print(f":: {Fore.BLUE}Encoded {Fore.MAGENTA}{amount_encoded}{Fore.RESET} image", end='')
        if amount_decoded != 1:
            print("s") # Add an 's' to the word 'image'
        elif amount_decoded == 1:
            print() # Only print a newline character
    
    if arguments.decode:
        # Print without a newline
        print(f":: {Fore.BLUE}Decoded {Fore.MAGENTA}{amount_decoded}{Fore.RESET} image", end='')
        if amount_decoded != 1:
            print("s") # Add an 's' to the word 'image'
        elif amount_decoded == 1:
            print() # Only print a newline character

if __name__ == "__main__":
    main()