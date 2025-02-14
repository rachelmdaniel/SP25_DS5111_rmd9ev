import sys
import re
import os
import pandas as pd
assert len(sys.argv) == 2
fname = sys.argv[1].strip()

def csv_normalizer(csvfile):
    assert os.path.splitext(csvfile)[1] == '.csv', (f"Not CSV file")
    directory, filename = os.path.split(os.path.abspath(csvfile))
    assert filename == "ygainers.csv" or filename == "wsjgainers.csv", (f"File cannot be used here. Check for typos and make sure it is called ygainers.csv or wsjgainers.csv")

    if "ygainers" in csvfile:
        def extract_first_number(text):
            match = re.match(r'^[\d.]+', text)
            return match.group(0) if match else None

        def extract_percentage(text):
            match = re.search(r'\d+\.?\d*', text)
            return match.group(0) if match else None

        y_raw = pd.read_csv("ygainers.csv")

        y_norm = y_raw[["Symbol","Price","Change","Change %"]]
        y_norm["Price"] = y_norm["Price"].apply(extract_first_number)
        y_norm["Change %"] = y_norm["Change %"].apply(extract_percentage)
        y_norm = y_norm.rename(columns = {'Symbol':'symbol','Price':'price','Change':'price_change','Change %':'price_percent_change'})

        assert y_norm.shape[1] == 4, (f"Incorrect number of columns")
        y_norm.to_csv('ygainers_norm.csv', index = False)

    elif "wsjgainers" in csvfile:
        def extract_symbol(text):
            match = re.search(r'\((.*?)\)', text)
            return match.group(1) if match else None

        wsj_raw = pd.read_csv("wsjgainers.csv")

        wsj_norm = wsj_raw[["Unnamed: 0","Last","Chg","% Chg"]]
        wsj_norm = wsj_norm.rename(columns = {'Unnamed: 0':'symbol','Last':'price','Chg':'price_change','% Chg':'price_percent_change'})
        extracted_symbol = [extract_symbol(row) for row in wsj_norm["symbol"]]
        wsj_norm["symbol"] = extracted_symbol

        assert wsj_norm.shape[1] == 4, (f"Incorrect number of columns")
        wsj_norm.to_csv('wsjgainers_norm.csv', index = False)

    else:
        print("There was no Yahoo gainers file or WSJ gainers file passed")

csv_normalizer(fname)
