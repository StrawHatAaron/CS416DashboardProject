import pandas as pd

total_filtered_df = pd.DataFrame()
csv_year_range = range(1990, 2023)  

# Loop through the specified years to load multiple CSV files
for year in csv_year_range:

    # Load the CSV file (replace 'your_file.csv' with the actual file name)
    # print(f"BLS\\{year}.annual.singlefile.csv")
    df = pd.read_csv(f"BLS\\{year}.annual.singlefile.csv")
    
    # Print the column names to verify the structure
    print(f"Columns in {year} CSV file:", df.columns.tolist())

    # Ensure the column exists before filtering
    if 'own_code' in df.columns:
        # Filter rows where 'own_code' is 0
        filtered_df = df[df['own_code'] == 0]
        # Concatenate the filtered DataFrame with the existing one
        total_filtered_df = pd.concat([total_filtered_df, filtered_df], ignore_index=True)

        print(len(total_filtered_df))

    else:
        print("Error: Column 'own_code' not found in the CSV file.")

print("Concatenated DataFrame:")
print(total_filtered_df)

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

total_filtered_df.to_csv('meta_BLS_average_income.csv', index=False)