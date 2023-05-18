#!/usr/bin/env python
"""The command-line interface for NoAI. This script should not be used as a module."""
import sys
import argparse
from imwatermark import WatermarkEncoder, WatermarkDecoder
from colorama import Fore

from no_ai import tree_utils
from no_ai import decode
from no_ai import encode


def main():
    """The required entry point for the `setup.py` script/"""

    # This variable determines what AI to watermark for
    watermark_type = "SDV2"  # In this case, Stable Diffusion v2.0

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--encode", action="store_true")
    argument_parser.add_argument("--decode", action="store_true")
    argument_parser.add_argument("--directory", type=str)
    arguments = argument_parser.parse_args()

    if len(sys.argv) <= 1:
        print(f":: {Fore.RED}Error{Fore.RESET}: No arguments have been provided!")
        argument_parser.print_help()
        sys.exit(1)

    amount_encoded: int = 0
    amount_decoded: int = 0

    if arguments.encode:
        encoder = WatermarkEncoder()
    if arguments.decode:
        decoder = WatermarkDecoder("bytes", 32)

    for file in tree_utils.branch_images(arguments.directory):
        if arguments.encode:
            encode.encode(file, encoder, watermark_type)
            amount_encoded += 1
        if arguments.decode:
            decode.decode(file, decoder)
            amount_decoded += 1

    # To do: Reduce code duplication

    if arguments.encode:
        # Print without a newline
        print(
            f":: {Fore.BLUE}Encoded {Fore.MAGENTA}{amount_encoded}{Fore.RESET} image",
            end="",
        )
        if amount_decoded != 1:
            print("s")  # Add an 's' to the word 'image'
        elif amount_decoded == 1:
            print()  # Only print a newline character

    if arguments.decode:
        # Print without a newline
        print(
            f":: {Fore.BLUE}Decoded {Fore.MAGENTA}{amount_decoded}{Fore.RESET} image",
            end="",
        )
        if amount_decoded != 1:
            print("s")  # Add an 's' to the word 'image'
        elif amount_decoded == 1:
            print()  # Only print a newline character


if __name__ == "__main__":
    main()
