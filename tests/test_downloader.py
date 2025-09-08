import pytest
from unittest.mock import patch, MagicMock
from resumeio_dl import download_resume, Extension


@pytest.fixture
def mock_resume_downloader():
    with patch('resumeio_dl.downloader.ResumeDownloader') as mock_downloader:
        instance = mock_downloader.return_value
        instance.generate_pdf.return_value = b'fake pdf content'
        yield mock_downloader


def test_download_resume_success(mock_resume_downloader, tmp_path):
    # Setup
    output_file = tmp_path / "test.pdf"
    
    # Execute
    result = download_resume(
        rendering_token="test_token",
        output_filename=str(output_file),
        image_size=3000,
        extension=Extension.jpeg
    )
    
    # Verify
    assert result is True
    assert mock_resume_downloader.called
    assert mock_resume_downloader.call_args[1]['rendering_token'] == "test_token"
    assert mock_resume_downloader.call_args[1]['image_size'] == 3000
    assert mock_resume_downloader.call_args[1]['extension'] == Extension.jpeg
    assert output_file.exists()


def test_download_resume_exception(mock_resume_downloader):
    # Setup
    mock_resume_downloader.return_value.generate_pdf.side_effect = Exception("Test error")
    
    # Execute
    result = download_resume(
        rendering_token="test_token",
        output_filename="test.pdf"
    )
    
    # Verify
    assert result is False
