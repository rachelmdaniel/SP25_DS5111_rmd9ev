from abc import ABC, abstractmethod

# DOWNLOADER
class GainerDownload(ABC):
    def __init__(self):
        self.url = url

    @abstractmethod
    def download(self):
        pass

# PROCESSOR 
class GainerProcess(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def normalize(self):
        pass

    @abstractmethod
    def save_with_timestamp(self):
        pass

