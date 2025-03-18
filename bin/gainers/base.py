from abc import ABC, abstractmethod

# DOWNLOADER
class GainerDownload(ABC):
    """ Abstract base class used to download gainer data. """

    def __init__(self,url):
        self.url = url

    @abstractmethod
    def download(self):
        """ Abstract method to ensure gainer data is downloaded from source. """
        raise NotImplementedError("Subclasses must implement download method.")

# PROCESSOR
class GainerProcess(ABC):
    """ Abstract base class for processing gainer data. """

    def __init__(self):
        raise NotImplementedError("Subclasses must implement init method.")

    @abstractmethod
    def normalize(self):
        """ Abstract method to ensure gainer data is normalized. """
        raise NotImplementedError("Subclasses must implement normalize method.")

    @abstractmethod
    def save_with_timestamp(self):
        """ Abstract method to ensure gainer data is downloaded from source. """
        raise NotImplementedError("Subclasses must implement save with timestamp  method.")

