"""Decode the invisible watermark."""

import cv2
from colorama import Fore


def decode(file, decoder):
    """Attempt to decode a watermark (of type `watermark_type`) from the given `file` variable"""

    print(f":: {Fore.BLUE}Decoding {Fore.MAGENTA}{file}{Fore.RESET}")

    image_file = cv2.imread(file)
    watermark = decoder.decode(image_file, "dwtDct")
    mark = watermark.decode("utf-8")
    # Check if there is a watermark
    if watermark != b"\x00\x00\x00\x00":
        print(
            f":: {Fore.MAGENTA}{file}{Fore.RESET} - Watermark: {mark}, {watermark.decode()}"
        )
    elif watermark == b"\x00\x00\x00\x00":
        print(
            f":: {Fore.YELLOW}Warning{Fore.RESET}: No watermark found for {Fore.MAGENTA}{file}{Fore.RESET}!"
        )
