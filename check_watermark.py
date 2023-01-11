import cv2
import os
from imwatermark import WatermarkDecoder

# Get all the PNG and JPG files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')]

decoder = WatermarkDecoder('bytes', 136)

# Loop through all the image files
for file in files:
    # Split the file name and extension
    bgr = cv2.imread(file)
    watermark = decoder.decode(bgr, 'dwtDct')
    mark = watermark.decode('utf-8')
    toPrint = '{} - watermark: {}, {}';
    print(toPrint.format(file,mark,watermark))