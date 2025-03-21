import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from get_gainer import ProcessGainer

# Mock downloader and normalizer
class MockDownloader:
    def __init__(self):
        self.download_called = False

    def download(self):
        self.download_called = True

class MockNormalizer:
    def __init__(self):
        self.normalize_called = False
        self.save_called = False

    def normalize(self):
        self.normalize_called = True

    def save_with_timestamp(self):
        self.save_called = True

# Test for ProcessGainer
def test_process_gainer():
    downloader = MockDownloader()
    normalizer = MockNormalizer()

    processor = ProcessGainer(downloader, normalizer)
    processor.process()

    assert downloader.download_called, "Download function was not called"
    assert normalizer.normalize_called, "Normalize function was not called"
    assert normalizer.save_called, "Save function was not called"
