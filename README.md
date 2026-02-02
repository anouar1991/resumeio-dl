# resumeio-dl

Download your resume.io resumes as **searchable, hyperlinked PDFs** — from the command line or Python.

resume.io doesn't let you export your own resume as a proper PDF unless you pay. This tool downloads the rendered pages, runs OCR to make the text searchable, and preserves all your hyperlinks. One command, done.

## Install

```bash
pip install resumeio-dl
```

You also need **Tesseract OCR** installed on your system:

```bash
# Ubuntu/Debian
sudo apt install tesseract-ocr

# macOS
brew install tesseract

# Windows — download from: https://github.com/UB-Mannheim/tesseract/wiki
```

## Quick Start

```bash
resumeio-dl YOUR_RENDERING_TOKEN
```

That's it. Your resume is saved as a PDF in the current directory.

### Options

```bash
resumeio-dl TOKEN -o my_resume.pdf    # custom filename
resumeio-dl TOKEN -s 4000             # higher resolution (default: 3000)
resumeio-dl TOKEN -e png              # png instead of jpeg
```

### Python API

```python
from resumeio_dl import download_resume, Extension

# Basic
download_resume("YOUR_RENDERING_TOKEN")

# Custom settings
download_resume(
    rendering_token="YOUR_RENDERING_TOKEN",
    output_filename="my_resume.pdf",
    image_size=4000,
    extension=Extension.png
)
```

## How to Find Your Rendering Token

1. Log in to [resume.io](https://resume.io)
2. Open browser DevTools (F12) → **Network** tab
3. Navigate to your resume list
4. Look for requests to `resume.io/api/app/resumes`
5. In the JSON response, find the `renderingToken` field (24-character string)

> **Tip:** You can also check `https://resume.io/api/app/cover-letters/` for cover letter tokens.

## What It Does

| Feature | Description |
|---------|-------------|
| **PDF export** | Downloads resume pages as images and converts to PDF |
| **Searchable text** | OCR via Tesseract makes the PDF text selectable and searchable |
| **Hyperlink preservation** | Clickable links from your resume are embedded in the PDF |
| **Multiple formats** | Supports JPEG, PNG, and WebP source images |
| **Configurable quality** | Adjust image resolution (1000–5000) for size vs. quality tradeoff |

## Requirements

- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

## Acknowledgements

Based on [resumeio-to-pdf](https://github.com/felipeall/resumeio-to-pdf) by [@felipeall](https://github.com/felipeall). This package adds a CLI, Python API, PyPI distribution, and hyperlink preservation.

## Contributing

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
