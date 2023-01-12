# NoAI

NO AI
(AI Watermark Generator)

Method 1:
How to use it with the exe file:

Download the release: [Latest Version](https://github.com/eballai/NoAI/releases/download/v1.0.0/NO_AI.Watermark.zip)

1. Place your PNG or JPG files to the same folder as the script.
2. Run the .exe file.
3. It will watermark each image and save it with a _wm suffix.
4. Copy the watermarked files elsewhere and delete the originals.

IMPORTANT: Backup your files!



Method2:
How to use it with the Python script:

1. Install Python
2. Go to the Python website https://www.python.org/downloads/
3. Download the latest stable release. It should automatically give you the correct installer for your OS.
4. Save the installer file to your computer
5. Follow the prompts to install Python.

On Windows, make sure to check the "Add Python to PATH" checkbox during the installation process.
Once the installation is complete, open a terminal window:
On Windows, you can do this by typing "cmd" into the Start menu search bar
On a Mac, you can do this by going to the Applications folder, then the Utilities folder, and clicking on the Terminal application
6. Type the following command and press Enter:
python3 --version
7. Download the zip file, and copy watermark.bat, watermark.py and watermark.scpt files to a new folder.


Watermarking Images (Recommended)
1. Copy your PNG or JPG files to the same folder as the script. Do not move the files!
2. Run the watermark command.
On Windows, this will be Watermark.bat file (Batch file). Simply double-click it.
On Mac, this will be a slightly different process:
Double-click on Watermark.scpt. This will launch the AppleScript editor.
3. Click the "Run" button to execute the script.
4. It will watermark each image and save it with a _wm suffix.
5. Copy the watermarked files elsewhere and delete the originals.

Watermarking Images (CLI method)

1. Copy your PNG or JPG files to the same folder as the script. Do not move the files!!
2. Open a terminal window.
On Windows, you can do this by typing "cmd" into the Start menu search bar
On a Mac, you can do this by going to the Applications folder, then the Utilities folder, and clicking on the Terminal application
3. In the terminal window, enter the following, and press Enter:
python watermark.py

It will watermark each image and save it with a _wm suffix.
4. Copy the watermarked files elsewhere and delete the originals.

## Background

This project is based on [Medium article](https://medium.com/@steinsfu/stable-diffusion-the-invisible-watermark-in-generated-images-2d68e2ab1241). It uses the open source [Invisible Watermark](https://github.com/ShieldMnt/invisible-watermark) project.


## Known Issue

This may not work with all AI art software. This targets Stable Diffusion and offshoots.
