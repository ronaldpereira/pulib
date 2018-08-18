import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pulib",
    version="1.0.0",
    author="Ronald Pereira",
    author_email="ronald.drp11@gmail.com",
    description="Positive-Unlabeled machine learning package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ronaldpereira/pulib",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
)
