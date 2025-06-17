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

# Check that there are 58 unique area_fips codes
if df['Area FIPs'].nunique() != 58:
    print(f"Warning: Expected 58 unique area_fips codes, found {df['Area FIPs'].nunique()}.")

# Create quartiles for the Median Household Income by each Year
df['Median Household Income Quartiles by each Year'] = df.groupby('Year')['Median Household Income'].transform(
    lambda x: pd.qcut(
        x, 4, labels=[
            'Low Median Household Income',
            'Lower Middle Median Household Income',
            'Upper Middle Median Household Income',
            'High Median Household Income'
        ]
    )
)

# Print the average of average_household_income by year and county
average_household_income_by_year = df.groupby(['County'])['Median Household Income'].mean()
# print("Average Household Income by year and county:")
# print(average_household_income_by_year)
# Save the average household income by year and county to a CSV file for validation
average_household_income_by_year.to_csv("Validation_Averages/Average_Household_Income_by_Year_and_County.csv", index=False)

# # Save the filtered DataFrame to a new CSV file
df.to_csv("Wrangled_DataUSA_California_County_Housing.csv", index=False)