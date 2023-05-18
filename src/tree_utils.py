import os


def branch(directory):
    for file in os.listdir():
        # Check if file exists
        if os.path.isfile(file):
            yield file


def branch_images(directory):
    for file in branch(directory):
        # Check the file extension
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            yield file
