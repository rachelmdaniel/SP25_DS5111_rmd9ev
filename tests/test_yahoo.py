import pandas as pd
import os
import sys
from unittest.mock import patch, MagicMock, mock_open

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo



# Test GainerDownloadYahoo

def test_yahoo_init():
    """Test Yahoo downloader initialization."""
    downloader = GainerDownloadYahoo()
    assert downloader.url == "https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200"


@patch("bin.gainers.yahoo.os.system")
@patch("bin.gainers.yahoo.os.path.exists", return_value=True)
@patch("bin.gainers.yahoo.os.path.getsize", return_value=100)
@patch("builtins.open", new_callable=mock_open)

def test_yahoo_download(mock_open_file,mock_exists, mock_getsize, mock_system):
    """Test Yahoo download function without downloading."""
    downloader = GainerDownloadYahoo()
    downloader.download()

    with open("ygainers.csv", "w") as f:
        f.write("Mock Data")

    assert os.path.exists("ygainers.csv"), "Mock download of file"

# Test GainerProcessYahoo

def test_yahoo_processor_normalize():
    """Test Yahoo normalize function processes data correctly."""

    # Test CSV file
    csv_filename = "ygainers.csv"
    data = {
        "Symbol": ["AAPL", "MSFT"],
        "Price": ["150.50", "300.75"],
        "Change": ["+2.50", "+5.00"],
        "Change %": ["+1.67%", "+2.34%"]
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_filename, index=False)

    processor = GainerProcessYahoo()
    processor.normalize()


    assert processor.y_norm is not None
    assert processor.y_norm.shape[1] == 4
    assert list(processor.y_norm.columns) == ["symbol", "price", "price_change", "price_percent_change"]
    assert processor.y_norm["symbol"].tolist() == ["AAPL", "MSFT"]

    os.remove(csv_filename)

def test_yahoo_processor_save():
    """Test yahoo save_with_timestamp function creates a file."""
    # Test CSV file
    csv_filename = "ygainers.csv"
    data = {
        "Symbol": ["AAPL", "MSFT"],
        "Price": ["150.50", "300.75"],
        "Change": ["+2.50", "+5.00"],
        "Change %": ["+1.67%", "+2.34%"]
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_filename, index=False)

    processor = GainerProcessYahoo()
    processor.normalize()
    processor.save_with_timestamp()

    files = [f for f in os.listdir() if f.startswith("ygainers_norm_") and f.endswith(".csv")]
    assert len(files) > 0, "No output file was created."

    os.remove(csv_filename)
    for i in files:
        os.remove(i)
