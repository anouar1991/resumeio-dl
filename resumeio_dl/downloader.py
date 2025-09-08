#!/usr/bin/env python3
"""
Module to download resumes from resume.io as PDF files.
"""

import io
import json
from datetime import datetime, UTC
import requests
from PIL import Image
import pytesseract
from pypdf import PdfReader, PdfWriter

# Different versions of pypdf have different imports for AnnotationBuilder
try:
    from pypdf import AnnotationBuilder
except ImportError:
    try:
        from pypdf.generic import AnnotationBuilder
    except ImportError:
        # Create a simple implementation if not available
        class AnnotationBuilder:
            @staticmethod
            def link(rect, url):
                from pypdf.generic import DictionaryObject, NameObject, NumberObject, TextStringObject, ArrayObject
                annotation = DictionaryObject()
                annotation[NameObject("/Type")] = NameObject("/Annot")
                annotation[NameObject("/Subtype")] = NameObject("/Link")
                annotation[NameObject("/Rect")] = ArrayObject([NumberObject(rect[0]), NumberObject(rect[1]), 
                                                              NumberObject(rect[2]), NumberObject(rect[3])])
                annotation[NameObject("/A")] = DictionaryObject()
                annotation[NameObject("/A")][NameObject("/Type")] = NameObject("/Action")
                annotation[NameObject("/A")][NameObject("/S")] = NameObject("/URI")
                annotation[NameObject("/A")][NameObject("/URI")] = TextStringObject(url)
                return annotation


class Extension:
    """Image extension types supported by resume.io"""
    jpeg = "jpeg"
    png = "png"
    webp = "webp"


class ResumeDownloader:
    """
    Class to download a resume from resume.io and convert it to a PDF.
    """
    def __init__(self, rendering_token, extension=Extension.jpeg, image_size=3000):
        """
        Initialize the downloader.
        
        Parameters
        ----------
        rendering_token : str
            Rendering Token of the resume to download.
        extension : str, optional
            Image extension to download, by default "jpeg".
        image_size : int, optional
            Size of the images to download, by default 3000.
        """
        self.rendering_token = rendering_token
        self.extension = extension
        self.image_size = image_size
        # Use timezone-aware datetime (fixes deprecation warning)
        self.cache_date = datetime.now(UTC).isoformat()[:-6] + "Z"
        self.METADATA_URL = f"https://ssr.resume.tools/meta/{rendering_token}?cache={self.cache_date}"
        self.IMAGES_URL = (
            f"https://ssr.resume.tools/to-image/{rendering_token}-{{page_id}}.{extension}"
            f"?cache={self.cache_date}&size={image_size}"
        )

    def generate_pdf(self):
        """
        Generate a PDF from the resume.io resume.
        
        Returns
        -------
        bytes
            PDF representation of the resume.
        """
        self._get_resume_metadata()
        images = self._download_images()
        pdf = PdfWriter()
        metadata_w, metadata_h = self.metadata[0].get("viewport").values()

        for i, image in enumerate(images):
            page_pdf = pytesseract.image_to_pdf_or_hocr(Image.open(image), extension="pdf", config="--dpi 300")
            page = PdfReader(io.BytesIO(page_pdf)).pages[0]
            page_scale = max(page.mediabox.height / metadata_h, page.mediabox.width / metadata_w)
            pdf.add_page(page)

            for link in self.metadata[i].get("links"):
                link_url = link.pop("url")
                link.update((k, v * page_scale) for k, v in link.items())
                x, y, w, h = link.values()

                annotation = AnnotationBuilder.link(rect=(x, y, x + w, y + h), url=link_url)
                pdf.add_annotation(page_number=i, annotation=annotation)

        with io.BytesIO() as file:
            pdf.write(file)
            return file.getvalue()

    def _get_resume_metadata(self):
        """Download the metadata for the resume."""
        response = self._get(self.METADATA_URL)
        content = json.loads(response.text)
        self.metadata = content.get("pages")

    def _download_images(self):
        """
        Download the images for the resume.
        
        Returns
        -------
        list[io.BytesIO]
            List of image files.
        """
        images = []
        for page_id in range(1, 1 + len(self.metadata)):
            image_url = self.IMAGES_URL.format(page_id=page_id)
            response = self._get(image_url)
            images.append(io.BytesIO(response.content))

        return images

    def _get(self, url):
        """
        Get a response from a URL.
        
        Parameters
        ----------
        url : str
            URL to get.
            
        Returns
        -------
        requests.Response
            Response object.
            
        Raises
        ------
        Exception
            If the response status code is not 200.
        """
        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/136.0.0.0 Safari/537.36",
            },
        )
        if response.status_code != 200:
            raise Exception(f"Unable to download resume (rendering token: {self.rendering_token}), "
                           f"status code: {response.status_code}")
        return response


def download_resume(rendering_token, output_filename=None, image_size=3000, extension=Extension.jpeg):
    """
    Download a resume from resume.io and save it as a PDF file.
    
    Parameters
    ----------
    rendering_token : str
        Rendering Token of the resume to download.
    output_filename : str, optional
        Name of the output PDF file. If not provided, the rendering token will be used.
    image_size : int, optional
        Size of the images to download, by default 3000.
    extension : str, optional
        Image extension to download, by default jpeg.
        
    Returns
    -------
    bool
        True if successful, False otherwise.
    """
    if not output_filename:
        output_filename = f"{rendering_token}.pdf"
    
    try:
        print(f"Downloading resume with rendering token: {rendering_token}")
        downloader = ResumeDownloader(
            rendering_token=rendering_token, 
            image_size=image_size,
            extension=extension
        )
        
        pdf_bytes = downloader.generate_pdf()
        
        with open(output_filename, "wb") as f:
            f.write(pdf_bytes)
        
        print(f"Resume successfully downloaded and saved to: {output_filename}")
        return True
    except Exception as e:
        print(f"Error downloading resume: {str(e)}")
        return False
