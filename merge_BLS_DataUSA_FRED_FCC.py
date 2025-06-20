# Aaron Miller - merge_BLS_DataUSA_FRED_FCC.py
# This script merges the wrangled data from BLS, DataUSA, and FRED for California counties.
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
mean_values = df.groupby('County').mean(numeric_only=True)
mean_values['Year'] = 'All Years'
print("Mean columns for All Years:")
print(mean_values.columns)
print(mean_values)
df = pd.concat([df, mean_values], ignore_index=True)




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

# Create quartiles for the Average Annual Wage by each Year
df['Annual_Wage_Quartiles_by_each_Year'] = df.groupby('Year')['Average Annual Wage'].transform(
    lambda x: pd.qcut(
        x, 4, labels=[
            'Low Average Annual Wage',
            'Lower Middle Average Annual Wage',
            'Upper Middle Average Annual Wage',
            'High Average Annual Wage'
        ]
    )
)


#Create quartiles for the Average Annual Wage by year
df['Bachelor DegOrHigher Quartiles by each Year'] = df.groupby('Year')['Percent of Adults with Bachelors or Higher'].transform(
    lambda x: pd.qcut(
        x, 4, labels=[
            'Lower Bachelors or Higher Education',
            'Lower Middle Bachelors or Higher Education',
            'Upper Middle Bachelors or Higher Education',
            'High Bachelors or Higher Education'
        ]
    )
)


# Sort for some manual validation with my eyes
df = df.sort_values(by=['Year']).reset_index(drop=True)


# write the merged DataFrame to a CSV file
df.to_csv('Merged_California_County_Data_BLS_DataUSA_FRED_FCC.csv', index=False)