import sys
sys.path.append('.')
import os
import re
import pandas as pd
from  bin.normalize_csv import csv_normalizer

def test_normalize_wsjgainers_csv():
        sample_file = os.path.join(os.path.dirname(__file__),"..", "sample_data","wsjgainers.csv")
        sample_file = os.path.abspath(sample_file).strip()

        print(f"Sample file path: {sample_file}")
        print(f"Extracted extension: {os.path.splitext(sample_file)[1]}")

        output_file = os.path.join(os.getcwd(), "wsjgainers_norm.csv")

        if os.path.exists(output_file):
                os.remove(output_file)

        csv_normalizer(sample_file)

        assert os.path.exists(output_file), "Normalized file not created"

        wsjnorm = pd.read_csv(output_file)
        assert "symbol" in wsjnorm.columns and "price_change" in wsjnorm.columns, "Missing expected columns"


        os.remove(output_file)
