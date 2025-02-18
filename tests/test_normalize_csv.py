import sys
sys.path.append('.')
import os
import re
import pandas as pd
from bin.normalize_csv import csv_normalizer

def test_normalize_csv(monkeypatch):
	sample_file = os.path.join(os.path.dirname(__file__),"..", "sample_data","ygainers.csv")
	sample_file = os.path.abspath(sample_file).strip()

	monkeypatch.setattr(sys, 'argv', ['test_normalize_csv', sample_file])

	print(f"file being passed in: {sys.argv[1].strip()}")
	print(f"Sample file path: {sample_file}")
	print(f"Extracted extension: {os.path.splitext(sample_file)[1]}")

	output_file = os.path.join(os.getcwd(), "ygainers_norm.csv")

	if os.path.exists(output_file):
		os.remove(output_file)

	csv_normalizer(sample_file)

	assert os.path.exists(output_file), f"Normalized file not created"

	ynorm = pd.read_csv(output_file)
	assert "symbol" in ynorm.columns and "price_change" in ynorm.columns, "Missing expected columns"


	os.remove(output_file)
