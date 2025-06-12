import pandas as pd


total_filtered_df = pd.DataFrame()
csv_year_range = range(1990, 2024)  

# Loop through the specified years to load multiple CSV files
for year in csv_year_range:

    # Load the CSV file (replace 'your_file.csv' with the actual file name)
    # print(f"BLS\\{year}.annual.singlefile.csv")
    df = pd.read_csv(f"BLS\\{year}.annual.singlefile.csv")
    
    # Print the column names to verify the structure
    # print(f"Columns in {year} CSV file:", df.columns.tolist())

    # Ensure the column exists before filtering
    if 'own_code' in df.columns:
        # Filter rows where 'own_code' is 0
        filtered_df = df[df['own_code'] == 0]
        # Concatenate the filtered DataFrame with the existing one
        total_filtered_df = pd.concat([total_filtered_df, filtered_df], ignore_index=True)

        # print(len(total_filtered_df))

    else:
        print("Error: Column 'own_code' not found in the CSV file.")

# print("Concatenated DataFrame:")
# print(total_filtered_df)

# Filter the DataFrame to keep only the specified columns
total_filtered_df = total_filtered_df[['area_fips', 
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
california_county_filtered_df = california_county_filtered_df[california_county_filtered_df['area_fips'].str.endswith('000') == False]

# Add state and county names to the DataFrame
county_names_df = pd.read_csv('fcc\\ca_fips_county_names.csv')
# Ensure the area_fips column in county_names_df is of type string and same format lenth for merge
county_names_df['area_fips'] = county_names_df['area_fips'].apply(lambda x: f'0{x}' if len(str(x)) == 4 else str(x))    


# Merge the county names DataFrame with the filtered California counties DataFrame
final_california_county_filtered_df = pd.merge(county_names_df, california_county_filtered_df, on='area_fips')

# Save the filtered DataFrame for California counties to a new CSV file
final_california_county_filtered_df.to_csv('meta_BLS_california_county_average_income.csv', index=False)

