# mine_BLS_FCC.py - Aaron Miller 
# This script processes multiple CSV files from the Bureau of Labor Statistics (BLS) to filter and 
# aggregate data for California counties from the Federal Communications Commission (FCC).
# Refer to the README.md for more information on the data sources and processing steps.
import pandas as pd

# Intialize an empty DataFrame outside the For loop scope
total_filtered_df = pd.DataFrame()
# Define the range of years for which Data USA and BLS CSV files are available and matching
csv_year_range = range(2010, 2024)  # can go from 1990 to 2023

# Loop through the specified years to load multiple CSV files
for year in csv_year_range:

    # Load the CSV file (replace 'your_file.csv' with the actual file name)
    df = pd.read_csv(f"BLS\\{year}.annual.singlefile.csv")
    
    # Ensure the column exists before filtering
    if 'own_code' in df.columns:
        # Filter rows where 'own_code' is 0
        filtered_df = df[df['own_code'] == 0]
        # Concatenate the filtered DataFrame with the existing one
        total_filtered_df = pd.concat([total_filtered_df, filtered_df], ignore_index=True)

    else:
        print("Error: Column 'own_code' not found in the CSV file.")

# Filter the DataFrame to keep only the specified columns
total_filtered_df = total_filtered_df[[
                                       'area_fips', 
                                       'own_code',
                                       'industry_code',
                                       'agglvl_code',
                                       'size_code',
                                       'year',
                                       'annual_avg_emplvl',
                                       'total_annual_wages',
                                       'taxable_annual_wages',
                                       'annual_contributions',
                                       'annual_avg_wkly_wage',
                                       'avg_annual_pay',
                                       'oty_total_annual_wages_chg',
                                       'oty_total_annual_wages_pct_chg',
                                       'oty_taxable_annual_wages_chg',
                                       'oty_taxable_annual_wages_pct_chg',
                                       ]]

# Pre-pend a 0 to the area_fips columns that have a length of 4
total_filtered_df['area_fips'] = total_filtered_df['area_fips'].apply(lambda x: f'0{x}' if len(str(x)) == 4 else str(x))

#Filter the DataFrame to only keep counties with a state_fips of '06' (California)
california_county_filtered_df = total_filtered_df[total_filtered_df['area_fips'].str.startswith("06")]
# Remove the state Level FIPs data as a whole
california_county_filtered_df = california_county_filtered_df[california_county_filtered_df['area_fips'].str.endswith('000') == False]

# Add state and county names to the DataFrame
county_names_df = pd.read_csv('FCC\\ca_fips_county_names.csv')
# Ensure the area_fips column in county_names_df is of type string and same format lenth for merge
county_names_df['area_fips'] = county_names_df['area_fips'].apply(lambda x: f'0{x}' if len(str(x)) == 4 else str(x))    

# Merge the county names DataFrame with the filtered California counties DataFrame
final_california_county_filtered_df = pd.merge(county_names_df, california_county_filtered_df, on='area_fips')

# Create quartiles for the Average Annual Wage by each Year
final_california_county_filtered_df['Annual_Wage_Quartiles_by_each_Year'] = final_california_county_filtered_df.groupby('year')['avg_annual_pay'].transform(
    lambda x: pd.qcut(
        x, 4, labels=[
            'Low Average Annual Wage',
            'Lower Middle Average Annual Wage',
            'Upper Middle Average Annual Wage',
            'High Average Annual Wage'
        ]
    )
)
 

# Print the average of avg_annual_pay for each year by county
average_annual_pay_by_year = final_california_county_filtered_df.groupby(['County'])['avg_annual_pay'].mean()
print("Average annual pay by year and county:")
print(average_annual_pay_by_year)
# Save the average annual pay by year and county to a CSV file for validation
average_annual_pay_by_year.to_csv("Validation_Averages/Average_Annual_Pay_by_Year_and_County.csv", index=False)

# Save the filtered DataFrame for California counties to a new CSV file
final_california_county_filtered_df.to_csv('Wrangled_BLS_California_County_Average_Income.csv', index=False)