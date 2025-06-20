# mine_DataUSA.py - Aaron Miller
# THis script processes a CSV file from DataUSA to filter and aggregate data for California counties,
# specifically focusing on median household and quartiles for that household income
import pandas as pd

# Load the CSV file from the DataUSA directory
df = pd.read_csv("DataUSA\\Income by Location.csv")

# Filter out race based data
df = df[df['Race'] == 'Total']

# Filter out uneeded columnss
df = df[[  
        'ID Year',
        'Household Income by Race', 
        'Household Income by Race Moe', 
        'Geography', 
        'ID Geography']]

# Rename some columns for clarity and drop some unnecessary ones
df.rename(columns={
    'ID Year': 'Year',
    'Household Income by Race': 'Median Household Income',
    'Household Income by Race Moe': 'Median Household Income Margin of Error',
    'Geography': 'County',
    'ID Geography': 'ID Geography',
}, inplace=True)

# Filter out the string ", CA" from the column 'County'
df['County'] = df['County'].str.replace(r', CA$', '', regex=True)

# # Add a new column for area_fips to represent the FIPS code
df['Area FIPs'] = df['ID Geography'].str.replace('05000US', '', regex=False)

# drop the 'ID Geography' column as it is no longer needed
df.drop(columns=['ID Geography'], inplace=True)

# Check that there are 58 unique area_fips codes
if df['Area FIPs'].nunique() != 58:
    print(f"Warning: Expected 58 unique area_fips codes, found {df['Area FIPs'].nunique()}.")


# # Save the filtered DataFrame to a new CSV file
df.to_csv("Wrangled_DataUSA_California_County_Housing.csv", index=False)