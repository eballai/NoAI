import os
from setuptools import find_packages, setup

with open("README.md", encoding="UTF-8") as readme:
    long_desc = readme.read()

if os.path.exists("src"):
    os.rename("src", "no-ai")

setup(
    name="no-ai",
    version="2.0.0",
    packages=find_packages(),
    include_package_data=True,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    description="Generate invisible AI watermarks.",
    author="eballai, MolassesLover",
    author_email="122407740+eballai@users.noreply.github.com, 60114762+MolassesLover@users.noreply.github.com",
    url="https://github.com/eballai/NoAI",
    install_requires=["colorama", "SCons", "opencv-python", "invisible-watermark"],
    license="MIT",
    entry_points={
        "console_scripts": [
            "no_ai = no_ai.cli:main",
        ]
    },
)

if os.path.exists("no-ai"):
    os.rename("no-ai", "src")