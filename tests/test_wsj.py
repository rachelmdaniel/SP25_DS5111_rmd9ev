import pytest
import pandas as pd
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ


# Test GainerDownloadWSJ

def test_wsj_init():
    """Test WSJ downloader initialization."""
    downloader = GainerDownloadWSJ()
    assert downloader.url == "https://www.wsj.com/market-data/stocks/us/movers"

@pytest.mark.flaky(reruns=3)
def test_wsj_download():
    """Test WSJ download function."""
    downloader = GainerDownloadWSJ()
    downloader.download()

    assert os.path.exists("wsjgainers.html")
    assert os.path.exists("wsjgainers.csv")

    os.remove("wsjgainers.html")
    os.remove("wsjgainers.csv")

# Test GainerProcessWSJ

def test_wsj_processor_normalize():
    """Test WSJ normalize function processes data correctly."""

    # Test CSV file
    csv_filename = "wsjgainers.csv"
    data = {
        "Unnamed: 0": ["Apple (AAPL)", "Microsoft (MSFT)"],
        "Last": [150.0, 300.0],
        "Chg": [2.5, 5.0],
        "% Chg": [1.5, 2.0]
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_filename, index=False)

    processor = GainerProcessWSJ()
    processor.normalize()

    assert processor.wsj_norm is not None
    assert processor.wsj_norm.shape[1] == 4
    assert list(processor.wsj_norm.columns) == ["symbol", "price", "price_change", "price_percent_change"]
    assert processor.wsj_norm["symbol"].tolist() == ["AAPL", "MSFT"]

    os.remove(csv_filename)

def test_wsj_processor_save():
    """Test WSJ save_with_timestamp function creates a file."""
    # Test CSV file
    csv_filename = "wsjgainers.csv"
    data = {
        "Unnamed: 0": ["Apple (AAPL)", "Microsoft (MSFT)"],
        "Last": [150.0, 300.0],
        "Chg": [2.5, 5.0],
        "% Chg": [1.5, 2.0]
    }

    df = pd.DataFrame(data)
    df.to_csv(csv_filename, index=False)

    processor = GainerProcessWSJ()
    processor.normalize()
    processor.save_with_timestamp()

    files = [f for f in os.listdir() if f.startswith("wsjgainers_norm_") and f.endswith(".csv")]
    assert len(files) > 0, "No output file was created."

    os.remove(csv_filename)
    for i in files:
        os.remove(i)
