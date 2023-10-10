# file: setup.py

import os
from pathlib import Path
from setuptools import find_packages, setup

PKG_FOLDER = Path(os.path.abspath(os.path.dirname(__file__)))

with open(PKG_FOLDER / "README.md") as f:
    long_description = f.read()


setup(
    name="dnd-roller",
    version="0.0.1",
    author="Dave, Bianca, Mahe, Valerio OR YOU",
    author_email="vmaggio@gmail.com OR YOURS",
    description="Python package to roll D&D dice in the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/leriomaggio OR YOUR-GITHUB_ID/dnd-roller",
    include_package_data=True,
    packages=find_packages(exclude=[]),
    install_requires=["tabulate"],
)
