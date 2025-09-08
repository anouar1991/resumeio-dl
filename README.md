# resumeio-dl

Download resumes from resume.io as PDF files without using the web UI.

## Installation

```bash
pip install resumeio-dl
```

### Requirements

- Python 3.8 or higher
- Tesseract OCR must be installed on your system

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

## How to find your renderingToken

1. Go to your resume on resume.io
2. Check the API response:
   - For resumes: https://resume.io/api/app/resumes
   - For cover letters: https://resume.io/api/app/cover-letters/
3. Find the `renderingToken` in the response

## Features

- Download resume images from resume.io
- Convert images to a searchable PDF with OCR
- Preserve hyperlinks from the original resume
- Support for different image formats and resolutions

## Acknowledgements

This project is based on the original [resumeio-to-pdf](https://github.com/felipeall/resumeio-to-pdf) repository by [felipeall](https://github.com/felipeall). The original project provides a web interface for downloading resumes from resume.io, while this package focuses on providing a command-line interface and Python API.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT
