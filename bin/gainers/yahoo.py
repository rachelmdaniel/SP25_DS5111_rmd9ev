"""
Module for Downloading and Processing yahoo data.
"""

import re
import os
from datetime import datetime
import pandas as pd
from .base import GainerDownload, GainerProcess


class GainerDownloadYahoo(GainerDownload):
    """
    Contains functions for downloading Yahoo gainers data.
    """

    def __init__(self):
        super().__init__("https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200")

    def download(self):
        print("Downloading yahoo gainers")
        success = False
        retries = 0
        max_retries = 5

        while not success and retries < max_retries:
            os.system("google-chrome-stable --headless --disable-gpu --dump-dom  --no-sandbox --timeout=5000 "
                      "'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html")
            if os.path.exists("ygainers.html") and os.path.getsize("ygainers.html") != 0:   # plus 1 for the error checking here nice
                os.system("python -c \"import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')\"")
                print("Yahoo gainers saved into CSV")
                success = True
            else:
                retries += 1
        if not success:
            raise RuntimeError("Failed to download yahoo gainers in 5 attempts.")   # I like the retry idea!  nice

class GainerProcessYahoo(GainerProcess):
    """
    Contains functions for processing Yahoo gainers data.
    """

    def __init__(self):
        super().__init__()
        self.y_norm = None

    def normalize(self):
        print("Normalizing yahoo gainers")
        csvfile = "ygainers.csv"

        def extract_first_number(text):
            text = str(text)
            match = re.match(r'^[\d.]+', text)
            return match.group(0) if match else None

        def extract_percentage(text):
            match = re.search(r'\d+\.?\d*', text)
            return match.group(0) if match else None

        y_raw = pd.read_csv(csvfile)

        y_norm = y_raw[["Symbol", "Price", "Change", "Change %"]]
        y_norm["Price"] = y_norm["Price"].apply(extract_first_number)
        y_norm["Change %"] = y_norm["Change %"].apply(extract_percentage)
        y_norm = y_norm.rename(columns={'Symbol': 'symbol', 'Price': 'price'})
        y_norm = y_norm.rename(columns={'Change': 'price_change', 'Change %': 'price_percent_change'})
        self.y_norm = y_norm

        assert y_norm.shape[1] == 4, "Incorrect number of columns"

    def save_with_timestamp(self):
        print("Saving Yahoo gainers")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'ygainers_norm_{timestamp}.csv'
        self.y_norm.to_csv(filename, index=False)
