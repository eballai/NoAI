import os
from setuptools import find_packages, setup

if os.path.exists("src"):
    os.rename("src", "no_ai")

setup()

if os.path.exists("no_ai"):
    os.rename("no_ai", "src")
