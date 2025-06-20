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


# Add new row named 'All Years' for column 'Year' that takes the average values of 
mean_values_df = df.groupby('County').mean(numeric_only=True)
mean_values_df['Year'] = 'All Years'








# Add state and county names to the DataFrame
county_names_df = pd.read_csv('FCC\\ca_fips_county_names.csv')

# rename 'area_fip,s' column to 'Area FIPs' for consistency
county_names_df = county_names_df.rename(columns={'area_fips': 'Area FIPs', 'County': 'County'})

# Merge the county names DataFrame with the filtered California counties DataFrame
mean_values_df = pd.merge(county_names_df, mean_values_df, on='Area FIPs')








# convert the 'Year' column to string type for consistency
mean_values_df['Year'] = mean_values_df['Year'].astype(str)
df['Year'] = df['Year'].astype(str)
df = pd.concat([df, mean_values_df], ignore_index=True)



# Create quartiles for the Average Annual Pay by each Year
df['Annual Wage Quartiles by each Year'] = df.groupby('Year')['Average Annual Pay'].transform(
    lambda x: pd.qcut(
        x, 4, labels=[
            'Low Average Annual Pay',
            'Lower Middle Average Annual Pay',
            'Upper Middle Average Annual Pay',
            'High Average Annual Pay'
        ]
    )
)

# Create numeric quartiles for the Average Annual Pay by each Year
df['Numeric Dollar Quartiles by each Year'] = df.groupby('Year')['Average Annual Pay'].transform(
    lambda x: pd.qcut(
        x, 4, labels=False #, retbins=True
    )
)

#Create quartiles for the Percent of Adults with Bachelors or Higher
df['Quartiles by each Year for Bachelor Degree or Higher'] = df.groupby('Year')['Percent of Adults with Bachelors or Higher'].transform(
    lambda x: pd.qcut(
        x, 4, labels=[
            'Lower Bachelors or Higher Education',
            'Lower Middle Bachelors or Higher Education',
            'Upper Middle Bachelors or Higher Education',
            'High Bachelors or Higher Education'
        ]
    )
)

# Create numeric quartiles for the Percent of Adults with Bachelors or Higher by each Year
df['Numeric Percentage Quartiles by each Year for Bachelor Degree or Higher'] = df.groupby('Year')['Percent of Adults with Bachelors or Higher'].transform(
    lambda x: pd.qcut(
        x, 4, labels=False #, retbins=True
    )
)

# Create quartiles for the Median Household Income by each Year
df['Quartiles by each Year for Median Household Income'] = df.groupby('Year')['Median Household Income'].transform(
    lambda x: pd.qcut(
        x, 4, labels=[
            'Low Median Household Income',
            'Lower Middle Median Household Income',
            'Upper Middle Median Household Income',
            'High Median Household Income'
        ]
    )
)

# Create numeric quartiles for the Median Household Income by each Year
df['Numeric Dollar Quartiles by each Year for Median Household Income'] = df.groupby('Year')['Median Household Income'].transform(
    lambda x: pd.qcut(
        x, 4, labels=False #, retbins=True
    )
)

# Sort for some manual validation with my eyes
df = df.sort_values(by=['Year', 'Area FIPs']).reset_index(drop=True)

# write the merged DataFrame to a CSV file
df.to_csv('Merged_California_County_Data_BLS_DataUSA_FRED_FCC.csv', index=False)