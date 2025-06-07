import pandas as pd

filtered_dataframes = pd.DataFrame()
csv_year_range = range(1990, 2023)  # Adjust the range as needed


# Loop through the specified years to load multiple CSV files
for year in csv_year_range:

    # Load the CSV file (replace 'your_file.csv' with the actual file name)
    print(f"BLS\\{year}.annual.singlefile.csv")
    df = pd.read_csv(f"BLS\\{year}.annual.singlefile.csv")

    # Ensure the column exists before filtering
    if 'own_code' in df.columns:
        # Filter rows where 'own_code' is 0
        filtered_df = df[df['own_code'] == 0]

        print("Filtered DataFrame with own_code = 0:")
        print(filtered_df)
        #filtered_dataframes.append(filtered_df)
        pd.concat([filtered_dataframes, filtered_df], ignore_index=True)

    else:
        print("Error: Column 'own_code' not found in the CSV file.")


filtered_dataframes.to_csv('meta_BLS_average_income.csv', index=False)



















# Ensure the column name is correct
# if 'area_fips' in df.columns:
#     # Get unique elements and store them in a list
#     unique_area_fips = df['area_fips'].unique()
    
#     # Convert to a DataFrame if needed
#     unique_df = pd.DataFrame(unique_area_fips, columns=['Unique Area FIPS'])
    
#     print("Unique values in 'area_fips' column:")
#     print(unique_area_fips)
    
#     print("\nTotal unique elements of area FIPs:", len(unique_area_fips))
# else:
#     print("Error: Column 'area_fips' not found in the CSV file.")


# if 'agglvl_code' in df.columns:
#     # Get unique values in the 'agglvl_code' column
#     unique_values = df['agglvl_code'].unique()

#     # Compute the sum of unique elements
#     total_sum = sum(unique_values)

#     # Find the minimum unique value
#     min_value = min(unique_values)

#     print(f"Sum of unique elements in 'agglvl_code': {total_sum}")
#     print(f"Minimum value in 'agglvl_code': {min_value}")
# else:
#     print("Error: Column 'agglvl_code' not found in the CSV file.")
