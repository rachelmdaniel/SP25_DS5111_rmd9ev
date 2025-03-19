"""
Module for initiating the download, processing,and saving of gainer files.

"""

class ProcessGainer:
    """
    Template Class containing functions that result in a saved and processed gainers file.

    """
    def __init__(self, gainer_downloader, gainer_normalizer):
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        """
        Function for downloading data.
        """
        self.downloader.download()

    def _normalize(self):
        """
        Function for normalizing data.
        """

        self.normalizer.normalize()

    def _save_to_file(self):
        """
        Function for saving data file with timestamp.
        """
        self.normalizer.save_with_timestamp()

    def process(self):
        """
        Function for processing source data.
        """

        self._download()
        self._normalize()
        self._save_to_file()

if __name__=="__main__":
    import sys
    from bin.gainers.factory import GainerFactory

    # Make our selection, 'one' choice
    choice = sys.argv[1].lower()

    # let our factory get select the family of objects for processing
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # create our process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()
