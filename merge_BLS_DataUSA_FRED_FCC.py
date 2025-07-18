# Aaron Miller - merge_BLS_DataUSA_FRED_FCC.py
# This script merges the wrangled data from BLS, DataUSA, and FRED for California counties.
# appends avarage values for all years, and creates quartiles for various metrics.
import pandas as pd
import os

#run the mining scripts to wrangle the data from BLS, DataUSA, FRED and FCC
os.system('python mine_BLS.py')
os.system('python mine_DataUSA.py')
os.system('python mine_FRED.py')

#load in the wrangled data from the three sources
# BLS, DataUSA, and FRED
df_BLS = pd.read_csv("Wrangled_BLS_California_County_Average_Income.csv")
df_DataUSA = pd.read_csv("Wrangled_DataUSA_California_County_Housing.csv")
df_FRED = pd.read_csv("Wrangled_FRED_California_County_Education.csv")

# Merge the county names DataFrame with the filtered California counties DataFrame
df = pd.merge(df_BLS, df_DataUSA, on=['County', 'Year', 'Area FIPs'], how='outer', suffixes=('_BLS', '_DataUSA'))

# Merge the FRED data with the existing DataFrame
df = pd.merge(df, df_FRED, on=['County', 'Year', 'Area FIPs'], how='outer', suffixes=('', '_FRED'))


# Add new row named 'All Years Average Avg' for column 'Year' that takes the average values of 
mean_values_df = df.groupby('County').mean(numeric_only=True)
mean_values_df['Year'] = 'All Years Average'
 
# Add state and county names to the DataFrame
county_names_df = pd.read_csv('FCC\\ca_fips_county_names.csv')

# rename 'area_fips' column to 'Area FIPs' for consistency
county_names_df = county_names_df.rename(columns={'area_fips': 'Area FIPs', 'County': 'County'})

# Merge the county names DataFrame with the filtered California counties DataFrame
mean_values_df = pd.merge(county_names_df, mean_values_df, on='Area FIPs')

# convert the 'Year' column to string type for consistency
mean_values_df['Year'] = mean_values_df['Year'].astype(str)
df['Year'] = df['Year'].astype(str)
df = pd.concat([df, mean_values_df], ignore_index=True)

# Create quartiles for the Average Annual Pay by each Year
df['Annual Wage Group'] = df.groupby('Year')['Average Annual Pay'].transform(
    lambda x: pd.qcut(
        x, 3, labels=[
            'Low',
            'Middle',
            'High'
        ]
    )
)

#Create quartiles for the Percent of Adults with Bachelors or Higher
df['Bachelor Degree or Higher Group'] = df.groupby('Year')['Percent of Adults with Bachelors or Higher'].transform(
    lambda x: pd.qcut(
        x, 3, labels=[
            'Low',
            'Middle',
            'High'
        ]
    )
)

# Create quartiles for the Median Household Income by each Year
df['Median Household Income Group'] = df.groupby('Year')['Median Household Income'].transform(
    lambda x: pd.qcut(
        x, 3, labels=[
            'Low',
            'Middle',
            'High'
        ]
    )
)

# Create quartiles for the "Over-the-Year Average Annual Pay Change" by each Year
df['OTY Average Annual Pay Change Group'] = df.groupby('Year')['Over-the-Year Average Annual Pay Change'].transform(
    lambda x: pd.qcut(
        x, 3, labels=[
            'Low',
            'Middle',
            'High'
        ]
    )
)

# Create quartiles for the "Annual Average Number of Workers Employed" by each Year
df['Annual Average Number of Workers Group'] = df.groupby('Year')['Annual Average Number of Workers Employed'].transform(
    lambda x: pd.qcut(
        x, 3, labels=[
            'Low',
            'Middle',
            'High'
        ]
    )
)

# Sort for some manual validation with my eyes
df = df.sort_values(by=['Year', 'Area FIPs']).reset_index(drop=True)

# write the merged DataFrame to a CSV file
df.to_csv('Merged_California_County_Data_BLS_DataUSA_FRED_FCC.csv', index=False)