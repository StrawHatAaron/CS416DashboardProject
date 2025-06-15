import pandas as pd

# Load the CSV file from the DataUSA directory
df = pd.read_csv("DataUSA\\Income by Location.csv")

# Filter out race based data
# filtered_df = df[df['Race'] == 'Total']

# Filter out uneeded columnss
df = df[[  
                'ID Year',
                'Race',
                'Household Income by Race', 
                'Household Income by Race Moe', 
                'Geography', 
                'ID Geography', 
                'Slug Geography']]

# Rename some columns for clarity and drop some unnecessary ones
df.rename(columns={
    'ID Year': 'Year',
    'Race': 'Race',
    'Household Income by Race': 'Median Household Income',
    'Household Income by Race Moe': 'Median Household Income Margin of Error',
    'Geography': 'County',
    'ID Geography': 'ID Geography',
    'Slug Geography': 'Slug County'
}, inplace=True)

# Filter out the string ", CA" from the column 'County'
df['County'] = df['County'].str.replace(r', CA$', '', regex=True)

# # Add a new column for area_fips to represent the FIPS code
df['area_fips'] = df['ID Geography'].str.replace('05000US', '', regex=False)

# # Save the filtered DataFrame to a new CSV file
df.to_csv("Wrangled_DataUSA_California_County_Housing.csv", index=False)