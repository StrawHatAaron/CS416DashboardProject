# mine_FRED.py - Aaron Miller
# This script processes an Excel file containing education data for California counties 
# from the Federal Reserve Economic Data (FRED) and performs various validations and transformations.
import pandas as pd

# Load the Excel file from the FRED directory data from 2010 to 2023
df = pd.read_excel('FRED\\CA_Education_by_County_over_Years.xlsx', sheet_name='Sheet1')

#filter out rows where year is less than 2013
df = df[df['Year'] >= 2013]


# Validation: Validate all 58 counties are present for each year
expected_counties = 58
for year in df['Year'].unique():
    # Count the number of unique counties for the current year
    counties_in_year = df[df['Year'] == year]['County'].nunique()
    # Check if all counties are present for index of year
    if counties_in_year != expected_counties:
        print(f"Warning: Not all counties are present for the year {year}. Expected {expected_counties}, found {counties_in_year}.")



# Validation:Validate the Year column is between 2010 and 2023
year_min = 2013
year_max = 2023
if df['Year'].min() > year_min or df['Year'].max() < year_max:
    print(f"Warning:Years must be between {year_min} and {year_max}. Found min: {df['Year'].min()}, max: {df['Year'].max()}.")

# Remove ', CA' from the County column
df['County'] = df['County'].str.replace(', CA$', '', regex=True)

# Add state and county names to the DataFrame
county_names_df = pd.read_csv('FCC\\ca_fips_county_names.csv')

# Merge the county names DataFrame with the filtered California counties DataFrame
merged_df = pd.merge(df, county_names_df, on='County')

# Give Percent column a more descriptive name
merged_df.rename(columns={
    'County': 'County',
    'Percent': 'Percent of Adults with Bachelors or Higher',
    'Year': 'Year',
    'area_fips': 'Area FIPs',
}, inplace=True)


# Save the merged DataFrame to a new CSV file
merged_df.to_csv("Wrangled_FRED_California_County_Education.csv", index=False)
