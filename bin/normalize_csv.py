"""
This module cleans and normalizes raw yahoo and wsj csv files.
"""

import sys
import re
import os
import pandas as pd

def csv_normalizer(csvfile):

    """
    Function that performs the normalization.
    Arguments: ygainers.csv or wsjgainers.csv file
    returns: normalized csv file titled ygainers_norm.csv or wsjgainers_norm.csv
    """
    print(f"Checking extension for:'{csvfile}'")
    print(f"Extracted Extension: {os.path.splitext(csvfile)[1]}")
    print(f"Inside csv_normalizer, received file path: '{csvfile}'")

    csvfile = csvfile.strip()
    assert os.path.splitext(csvfile)[1].lower() == '.csv', "Not CSV file"

    filename = os.path.split(os.path.abspath(csvfile))[1]
    assert filename in ("ygainers.csv","wsjgainers.csv"),"Check file name."


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
        y_norm = y_norm.rename(columns = {'Symbol':'symbol','Price':'price'})
        y_norm = y_norm.rename(columns={'Change':'price_change','Change %':'price_percent_change'})

        assert y_norm.shape[1] == 4, "Incorrect number of columns"
        y_norm.to_csv('ygainers_norm.csv', index = False)

    elif "wsjgainers" in csvfile:
        def extract_symbol(text):
            match = re.search(r'\((.*?)\)', text)
            return match.group(1) if match else None

        wsj_raw = pd.read_csv("wsjgainers.csv")

        wsj_norm = wsj_raw[["Unnamed: 0","Last","Chg","% Chg"]]
        wsj_norm = wsj_norm.rename(columns = {'Unnamed: 0':'symbol','Last':'price'})
        wsj_norm = wsj_norm.rename(columns = {'Chg':'price_change','% Chg':'price_percent_change'})
        extracted_symbol = [extract_symbol(row) for row in wsj_norm["symbol"]]
        wsj_norm["symbol"] = extracted_symbol

        assert wsj_norm.shape[1] == 4, "Incorrect number of columns"
        wsj_norm.to_csv('wsjgainers_norm.csv', index = False)

    else:
        print("There was no Yahoo gainers file or WSJ gainers file passed")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bin/normalize_csv.py <path_to_csv>")
        sys.exit(1)

    fname = sys.argv[1].strip()
    csv_normalizer(fname)
