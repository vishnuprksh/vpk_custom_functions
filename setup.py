from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="vpk",  # Replace with your package name
    version="0.0.1",  # Initial release version
    author="Vishnu Prakash",
    author_email="vishnucheppanam@gmail.com",
    description="Contains custom functions which are used repeatedly during development",
    url="https://github.com/vishnuprksh/vpk",  # Replace with your package URL
    packages=find_packages(),
    download_url="https://github.com/vishnuprksh/vpk/archive/refs/tags/0.0.1.tar.gz",
    install_requires=[            # I get to this in a second
        'IPython',
        'pandas',
        'os',
        'warnings',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)