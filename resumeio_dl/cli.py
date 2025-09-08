#!/usr/bin/env python3
"""
Command-line interface for resumeio-dl
"""

import sys
import argparse
from resumeio_dl import download_resume, Extension


def main():
    """Main entry point for the CLI"""
    parser = argparse.ArgumentParser(
        description="Download a resume from resume.io as a PDF file."
    )
    parser.add_argument(
        "rendering_token",
        help="The rendering token of the resume (24-character string found in resume.io API responses)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output filename (default: <rendering_token>.pdf)",
        default=None
    )
    parser.add_argument(
        "-s", "--size",
        help="Image size to download (default: 3000)",
        type=int,
        default=3000
    )
    parser.add_argument(
        "-e", "--extension",
        help="Image extension to download (default: jpeg)",
        choices=["jpeg", "png", "webp"],
        default="jpeg"
    )
    
    args = parser.parse_args()
    
    # Map extension string to Extension class attribute
    ext_map = {
        "jpeg": Extension.jpeg,
        "png": Extension.png,
        "webp": Extension.webp
    }
    
    success = download_resume(
        rendering_token=args.rendering_token,
        output_filename=args.output,
        image_size=args.size,
        extension=ext_map[args.extension]
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
