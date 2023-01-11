import cv2
import os
from imwatermark import WatermarkEncoder

# Get all the PNG and JPG files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')]

wm = 'StableDiffusionV1'
encoder = WatermarkEncoder()
encoder.set_watermark('bytes', wm.encode('utf-8'))

# Loop through all the image files
for file in files:
    # Split the file name and extension
    file_name, file_ext = os.path.splitext(file)

    bgr = cv2.imread(file)
    bgr_encoded = encoder.encode(bgr, 'dwtDct')
    cv2.imwrite(file_name + '_wm' + file_ext, bgr_encoded)