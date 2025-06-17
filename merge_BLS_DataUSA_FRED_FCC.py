# Aaron Miller - merge_BLS_DataUSA_FRED_FCC.py
# This script merges the wrangled data from BLS, DataUSA, and FRED for California counties.
import pandas as pd

#load in the wrangled data from the three sources
# BLS, DataUSA, and FRED
df_BLS = pd.read_csv("Wrangled_BLS_California_County_Average_Income.csv")
df_DataUSA = pd.read_csv("Wrangled_DataUSA_California_County_Housing.csv")
df_FRED = pd.read_csv("Wrangled_FRED_California_County_Education.csv")

# Merge the county names DataFrame with the filtered California counties DataFrame
df = pd.merge(df_BLS, df_DataUSA, on=['County', 'Year', 'Area FIPs'], how='outer', suffixes=('_BLS', '_DataUSA'))

# Merge the FRED data with the existing DataFrame
df = pd.merge(df, df_FRED, on=['County', 'Year', 'Area FIPs'], how='outer', suffixes=('', '_FRED'))

# write the merged DataFrame to a CSV file
df.to_csv('Merged_California_County_Data_BLS_DataUSA_FRED_FCC.csv', index=False)