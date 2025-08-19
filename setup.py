#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   setup.py    
@Contact :   haoheliu@gmail.com
@License :   (C)Copyright 2020-2100

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
9/6/21 5:16 PM   Haohe Liu      1.0         None
"""

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = "ssr_eval"
DESCRIPTION = "This package is written for the evaluation of speech super-resolution algorithms."
URL = "https://github.com/haoheliu/ssr_eval"
EMAIL = "haoheliu@gmail.com"
AUTHOR = "Haohe Liu"
REQUIRES_PYTHON = ">=3.10.0"
VERSION = "0.0.6"

# Required packages for this module to be executed
REQUIRED = [
    "tqdm",
    "librosa",
    "soundfile",
    "scikit-image",
    # "Wave>=0.1.0",
    "torch>=2.1.0",
    "torchlibrosa>=0.0.7"
]

# Optional packages
EXTRAS = {}

# Get the absolute path of the directory containing this file
here = os.path.abspath(os.path.dirname(__file__))

# Import the README for the long description
try:
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints messages in bold."""
        print(f"\033[1m{s}\033[0m")

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system(f"{sys.executable} setup.py sdist bdist_wheel --universal")

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system(f"git tag v{about['__version__']}")
        os.system("git push --tags")

        sys.exit()


# Setup configuration
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=["sr_eval_vctk"],
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    cmdclass={
        "upload": UploadCommand,
    },
)
