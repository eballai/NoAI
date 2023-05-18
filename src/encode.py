import os
import cv2
from colorama import Fore
from imwatermark import WatermarkEncoder, WatermarkDecoder

def encode(file, encoder, watermark_type):
    print(f":: {Fore.BLUE}Encoding {Fore.MAGENTA}{file}{Fore.RESET}")

    encoder.set_watermark("bytes", watermark_type.encode("utf-8"))

    # Split the file name and extension
    file_name, file_extension = os.path.splitext(file)

    image_file = cv2.imread(file)
    image_file_encoded = encoder.encode(image_file, "dwtDct")
    cv2.imwrite(f"{file_name}-watermarked{file_extension}", image_file_encoded)