
"""
Contains the WSJ downloader and processing classes.

"""

import re
import os
from datetime import datetime
import pandas as pd
from .base import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
    """
    Contains functions for downloading WSJ gainers data.
    """

    def __init__(self):
        super().__init__("https://www.wsj.com/market-data/stocks/us/movers")

    def download(self):
        print("Downloading WSJ gainers")
        os.system("sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 "
                  "'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html")
        os.system("python -c \"import pandas as pd; raw = pd.read_html('wsjgainers.html'); raw[0].to_csv('wsjgainers.csv')\"")
        print("WSJ gainers saved into CSV")

class GainerProcessWSJ(GainerProcess):
    """
    Contains functions for processing WSJ gainers data.
    """

    def __init__(self):
        super().__init__()
        self.wsj_norm = None
    def normalize(self):
        print("Normalizing WSJ gainers")
        csvfile = "wsjgainers.csv"

        def extract_symbol(text):
            match = re.search(r'\((.*?)\)', text)
            return match.group(1) if match else None

        wsj_raw = pd.read_csv(csvfile)

        wsj_norm = wsj_raw[["Unnamed: 0","Last","Chg","% Chg"]]
        wsj_norm = wsj_norm.rename(columns = {'Unnamed: 0':'symbol','Last':'price'})
        wsj_norm = wsj_norm.rename(columns = {'Chg':'price_change','% Chg':'price_percent_change'})
        extracted_symbol = [extract_symbol(row) for row in wsj_norm["symbol"]]
        wsj_norm["symbol"] = extracted_symbol
        self.wsj_norm = wsj_norm

        assert wsj_norm.shape[1] == 4, "Incorrect number of columns"

    def save_with_timestamp(self):
        print("Saving WSJ gainers")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'wsjgainers_norm_{timestamp}.csv'
        self.wsj_norm.to_csv(filename, index=False)
