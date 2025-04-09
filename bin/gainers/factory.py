"""
Contains the important class GainerFactory for downloading and
processing gainer data based on the selected source (SRC).

"""
from .yahoo import GainerDownloadYahoo, GainerProcessYahoo
from .wsj import GainerDownloadWSJ, GainerProcessWSJ

class GainerFactory:

    """
    Factory class for creating gainer objects.

    """
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        """
        Function captures downloader function depending on source chosen.
        """
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()

    def get_processor(self):
        """
        Function captures processor function depending on source chosen.
        """
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        elif self.choice == 'wsj':
            return GainerProcessWSJ()
