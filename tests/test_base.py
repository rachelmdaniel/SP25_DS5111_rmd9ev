import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from bin.gainers.base import GainerDownload, GainerProcess

# Mock classes to test concrete implementation

class MockGainerDownload(GainerDownload):
    def download(self):
        return "Mock download successful."

class MockGainerProcess(GainerProcess):
    def normalize(self):
        return "Mock normalization successful."

    def save_with_timestamp(self):
        return "Mock save with timestamp successful."


def test_mock_gainer_download():
    """Ensure MockGainerDownload correctly implements the abstract class."""
    mock_downloader = MockGainerDownload("http://example.com")
    assert mock_downloader.download() == "Mock download successful."
    assert mock_downloader.url == "http://example.com"

def test_mock_gainer_process():
    """Ensure MockGainerProcess correctly implements the abstract class."""
    mock_processor = MockGainerProcess()
    assert mock_processor.normalize() == "Mock normalization successful."
    assert mock_processor.save_with_timestamp() == "Mock save with timestamp successful."
