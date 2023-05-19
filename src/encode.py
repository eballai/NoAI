"""Encode an invisible watermark into your image"""

import os
import cv2
from colorama import Fore


def encode(file, encoder, watermark_type):
    """Encode a watermark (of type `watermark_type`) into a copy of the given file."""

    print(f":: {Fore.BLUE}Encoding {Fore.MAGENTA}{file}{Fore.RESET}")

    encoder.set_watermark("bytes", watermark_type.encode("utf-8"))

    # Split the file name and extension
    file_name, file_extension = os.path.splitext(file)

    image_file = cv2.imread(file)
    image_file_encoded = encoder.encode(image_file, "dwtDct")
    cv2.imwrite(f"{file_name}-watermarked{file_extension}", image_file_encoded)
