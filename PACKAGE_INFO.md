# Python Package: resumeio-dl

I've created a Python package called `resumeio-dl` that allows you to download resumes from resume.io as PDF files without using the web UI. The package is ready to be published to PyPI.

## Package Structure

```
resumeio-dl/
├── LICENSE                  # MIT License
├── README.md                # Package documentation
├── pyproject.toml           # Build system configuration
├── resumeio_dl/             # Package source code
│   ├── __init__.py          # Package initialization
│   ├── cli.py               # Command-line interface
│   └── downloader.py        # Core functionality
└── setup.py                 # Package metadata and dependencies
```

## Features

- Download resume images from resume.io
- Convert images to a searchable PDF with OCR
- Preserve hyperlinks from the original resume
- Support for different image formats and resolutions
- Command-line interface (CLI)
- Python API for programmatic use

## Installation Instructions

Once published to PyPI, users will be able to install the package with:

```bash
pip install resumeio-dl
```

The package has the following dependencies:
- Python 3.8 or higher
- Pillow (for image processing)
- pytesseract (for OCR)
- pypdf (for PDF manipulation)
- requests (for HTTP requests)
- Tesseract OCR (system dependency)

## Usage

### Command Line Interface

```bash
# Basic usage with just the token
resumeio-dl YOUR_RENDERING_TOKEN

# Specify an output filename
resumeio-dl YOUR_RENDERING_TOKEN -o my_resume.pdf

# Change the image size for higher/lower quality
resumeio-dl YOUR_RENDERING_TOKEN -s 4000

# Change the image extension
resumeio-dl YOUR_RENDERING_TOKEN -e png
```

### Python API

```python
from resumeio_dl import download_resume, Extension

# Basic usage
download_resume("YOUR_RENDERING_TOKEN")

# Advanced usage
download_resume(
    rendering_token="YOUR_RENDERING_TOKEN",
    output_filename="my_resume.pdf",
    image_size=4000,
    extension=Extension.png
)
```

## Publishing Steps

To publish the package to PyPI:

1. Create an account on PyPI if you don't already have one
2. Set up your API token in ~/.pypirc or use environment variables
3. Use twine to upload the package:

```bash
python -m twine upload dist/*
```

## Improvements Made from Original Script

1. Fixed the UTC datetime deprecation warning
2. Improved error handling
3. Added proper command-line argument parsing
4. Added better documentation and type hints
5. Made the code more maintainable and modular
6. Added support for different image formats
7. Made the package installable via pip
