import pandas as pd
from pathlib import Path


# Week 1 Delibs Dataset


DATA_DIR = Path("data")
OUTPUT_DIR =Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

files_sold= sorted(DATA_DIR.glob("CRMLSSold*.csv"))
files_listing = sorted(DATA_DIR.glob("CRMLSListing*.csv"))
print("Sold files found:", len(files_sold))
print("Listing files found:", len(files_listing))

sold = pd.concat(
    [pd.read_csv(file, low_memory=False) for file in files_sold],
    ignore_index=True)
listings = pd.concat(
    [pd.read_csv(file, low_memory= False) for file in files_listing],
    ignore_index=True)
print("Sold rows after concatenation:", len(sold))
print("Listings rows after concatenation:", len(listings))

# Only Resident

sold_residential = sold[sold["PropertyType"] == "Residential"]
listings_residential = listings[listings["PropertyType"] == "Residential"]
print("Sold rows after Residential filter:", len(sold_residential))
print("Listings rows after Residential filter:", len(listings_residential))

#CSV files
sold_residential.to_csv("outputs/sold_combined_residential.csv", index=False)
listings_residential.to_csv("outputs/listings_combined_residential.csv", index=False)
print("Complete")