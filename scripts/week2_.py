#Reload data


import pandas as pd

sold =pd.read_csv("outputs/sold_combined_residential.csv", low_memory=False)
listings = pd.read_csv("outputs/listings_combined_residential.csv", low_memory=False)

print("week2 validation")

# Unique property types
print("\nSold property types:")
print(sold["PropertyType"].value_counts(dropna=False))

print("\nListings property types:")
print(listings["PropertyType"].value_counts(dropna=False))

#the filtering logic
sold_residential = sold[sold["PropertyType"] == "Residential"]
listings_residential = listings[listings["PropertyType"] == "Residential"]

print("\nSold rows before filter:", len(sold))
print("Sold rows after Residential filter:", len(sold_residential))
print("\nListings rows before filter:", len(listings))
print("Listings rows after Residential filter:", len(listings_residential))


# null-count table
sold_missing =pd.DataFrame({
    "missing_count": sold_residential.isnull().sum(),
    "missing_percent": sold_residential.isnull().mean() * 100})
listings_missing = pd.DataFrame({
    "missing_count": listings_residential.isnull().sum(),
    "missing_percent": listings_residential.isnull().mean() * 100})

print("\nSold null-count summary:")
print(sold_missing)

print("\nListings null-count summary:")
print(listings_missing)



#  Columns above 90% null
print("\nSold columns above 90% null:")
print(sold_missing[sold_missing["missing_percent"] > 90])
print("\nListings columns above 90% null:")
print(listings_missing[listings_missing["missing_percent"] > 90])

# Numeric distribution summaries
numeric_topics = ["ClosePrice", "LivingArea", "DaysOnMarket"]

print("\nSold numeric summary:")
print(sold_residential[numeric_topics].describe())

print("\nListings numeric summary:")
print(listings_residential[numeric_topics].describe())

# new CSVs
sold_residential.to_csv("outputs/sold_week2_filtered.csv", index=False)
listings_residential.to_csv("outputs/listings_week2_filtered.csv", index=False)
print("\ncomplete")
