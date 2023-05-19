"""Utility functions for dealing with file trees."""

import os


def branch(directory):
    """Loop through the files within the given directory."""

    for file in os.listdir(directory):
        # Check if file exists
        if os.path.isfile(file):
            yield file


def branch_images(directory):
    """Loop through the image files within the given directory."""

    for file in branch(directory):
        # Check the file extension
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            yield file
