#! /usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colorlib_check",
    version="1.0.0",
    author="Oliver \"c0rp3n\" Hitchcock",
    author_email="",
    description="Checks plugins and translation files for bad color tags.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c0rp3n/colorlib-check",
    packages= ['colorlib_check'],
    entry_points= {
        'console_scripts': [
            'colorlib_check = colorlib_check.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
