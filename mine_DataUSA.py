import pandas as pd

# Load the CSV file from the DataUSA directory
df = pd.read_csv("DataUSA\\Income by Location.csv")

# Filter out race based data
filtered_df = df[df['Race'] == 'Total']

# Filter out uneeded columnss
filtered_df = filtered_df[['ID Year',
                           'Household Income by Race', 
                           'Household Income by Race Moe', 
                           'Geography', 
                           'ID Geography', 
                           'Slug Geography']]

# Rename some columns for clarity and drop some unnecessary ones
filtered_df.rename(columns={
    'ID Year': 'Year',
    'Household Income by Race': 'Median Household Income',
    'Household Income by Race Moe': 'Median Household Income Margin of Error',
    'Geography': 'County',
    'ID Geography': 'ID Geography',
    'Slug Geography': 'Slug County'
}, inplace=True)

# Filter out the string ", CA" from the column 'County'
filtered_df['County'] = filtered_df['County'].str.replace(r', CA$', '', regex=True)

# Add a new column for area_fips to represent the FIPS code
filtered_df['area_fips'] = filtered_df['ID Geography'].str.replace('05000US', '', regex=True)

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv("meta_DataUSA_ca_county_housing.csv", index=False)