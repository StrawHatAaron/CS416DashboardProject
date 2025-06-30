# Past Decade California Counties Education and Earnings

## Aaron Miller -  CS 416 Data Visualization - Dashboard Project - Summer 2025 - Professor John C. Hart

---------------------------------------------------------------------------------------------------------------------

## Final Table: `Merged_California_County_Data_BLS_DataUSA_FRED_FCC.csv`

Created by `merge_BLS_DataUSA_FRED_FCC.py`. This merges Table 1, 2 and 3 from below into one table. This file's Attribute/Column names are meant to be self explanatory. Explanation for some of the fields can be seen below. All the Low, Middle and High cuts of data by each year are created here.

---------------------------------------------------------------------------------------------------------------------

## Table 1: `Wrangled_FRED_California_County_Education.csv`

### Source: *FRED - Federal Reserve Bank of St. Louis*

Data sets were gathered and wrangled from years 2010 to 2023. Below shows the approach used to create Table 1.

1. [Bachelor's Degree or Higher (5-year estimate) by California County](https://fred.stlouisfed.org/release/tables?rid=330&eid=391686)
2. Copied Data into Excel (`FRED\CA_Education_by_County_over_Years.xlsx`)
3. `mine_FRED.py` validates and wrangles data from the Excel file in step 2,
    adds `area_fips` attribute by mapping County name data derived from the
    [Federal Comminication Commission](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt) (`FCC\ca_fips_county_names.csv`)
    and creates final Table 1.

Attributes in  Table 1

| Attribute Name| Attribute Definition|
| :------- | :----------------- |
|**County**| CA Counties|
|**Percent of Adults with Bachelors or Higher**| Predicted percent of adult population that recieved a bachelors degree or higher.|
|**Year**| The year the data was gathered for that record|
|**Area FIPs**| Geographic County locations within California|
|**Bachelor DegOrHigher Quartiles by each Year**| Quartiles for Percent_of_Adults_with_Bachelors_or_Higher respective to that year|

---------------------------------------------------------------------------------------------------------------------

## Table 2: `Wrangled_DataUSA_California_County_Housing.csv`

### Source: *Data USA*

Data sets were gathered and wrangled for years 2013 to 2023 from Data USA. Below shows the approach used to create Table 2: `Wrangled_DataUSA_California_County_Housing.csv`.

1. [Data USA &rarr; California Geography &rarr; Housing and Living &rarr; Equity](https://datausa.io/profile/geo/california?measureWorkforceGeomap=wage&pums5RacesWorkforce=pums5Race0&yearlyChangeWorkforceGeomap=value#equity) &rarr; View Data &rarr; Download as CSV
2. Downloaded Data into `DataUSA\Income by Location.csv`
3. `mine_DataUSA.py` wragnles and validates data in CSV file from step 2 and creates the final Table 2.

Attributes in  Table 2

| Attribute Name| Attribute Definition|
| :-------| :-----------------|
| **Year**| The year the data was gathered for that record|
|**Median Household Income**| Median Household Income in US Dollars for that Race, County and Year record|
| **Median Household Income Margin of Error**| Median Household Income Margin of Error|
|**County**| Any of the 58 Counties in California|
|**ID Geography**| Global Geographic Identifier|
|**Area FIPs**| Geographic County locations within California|
|**Median Household Income Quartiles by each Year**| For each year a respective Median Household Income Quartile is assigned|

---------------------------------------------------------------------------------------------------------------------

## Table 3: `Wrangled_BLS_California_County_Average_Income.csv`

### Source:  *BLS - Bureau of Labor Statistics*

Data sets were gathered and wrangled from years 1990 to 2023. Below shows the approach used to create Table 3.

1. [Quarterly Census of Employment and Wages &rarr; QCEW NAICS-Based Data Files (1975 - most recent)](https://www.bls.gov/cew/downloadable-data-files.htm)
2. Downloaded CSVs Single Files &rarr; Annual Averages (`BLS\[1990-2023].annual.singlefile.csv`)
3. `mine_BLS.py` validates and wrangles data from the CSV files in step 2,
    adds `County` attribute by mapping Area FIP Codes derived from the
    [Federal Comminication Commission](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt) (`FCC\ca_fips_county_names.csv`)
    and creates final Table 3.

Attributes in Table 3 derived from these [Definitions](https://www.bls.gov/cew/about-data/downloadable-file-layouts/annual/naics-based-annual-layout.htm)

| Attribute Name| Attribute Definition |
| :-------| :---|
|**Area FIPs**| Was area_fips. This refers to the geographic location. I have only kept California county FIPs codes 06001 to 06115. |
|**County**| Merged with FCC data. Any of the 58 Counties in California|
|**Year**| Was year. this is respective of each year we are mining the data for- capped at year 2009 due to <https://www.fhfa.gov/data/pudb> having started recording this|
|**Annual Average Number of Workers Employed**| Was annual_avg_emplvl. Annual average of monthly employment levels for a given year. This represents the average number of workers in the county.|
|**Total Annual Wages**| Was total_annual_wages. Sum of the four quarterly total wage levels for a given year |
|**Taxable Annual Wages**| Was taxable_annual_wages. Sum of the four quarterly total taxable wage totals for a given year |
|**Annual Contributions**| Was annual_contributions. Sum of the four quarterly contribution totals for a given year |
|**Annual Average Weekly Wages**| Was annual_avg_wkly_wage. Average weekly wage based on the 12-monthly employment levels and total annual wage levels. |
|**Average Annual Pay**| Was avg_annual_pay. Average annual pay based on employment and wage levels for a given year. |
|**Over-the-Year Total Annual Wages Change**| Was oty_total_annual_wages_chg. Over-the-year change in the total annual wages for a given year |
|**Over-the-Year Total Annual Wages Percent Change**| Was oty_total_annual_wages_pct_chg. Over-the-year percent change in total annual wages for a given year (Rounded to the tenths place) |
|**Over-the-Year Taxable Annual Wages Change**| Was oty_taxable_annual_wages_chg. Over-the-year change in taxable annual wages for a given year |
|**Over-the-Year Taxable Annual Wages Percent Change**| Was oty_taxable_annual_wages_pct_chg. Over-the-year percent change in taxable annual wages for a given year (Rounded to the tenths place)|
|**Over-the-Year Average Annual Pay Change**| Was oty_avg_annual_pay_chg. Over-the-year change in taxable annual wages for a given year |
|**Over-the-Year Average Annual Pay Percent Change**| Was oty_avg_annual_pay_pct_chg. Over-the-year percent change in taxable annual wages for a given year (Rounded to the tenths place)|

---------------------------------------------------------------------------------------------------------------------

## Other Sources

Federal Communication Commission: <https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt>

------------------------------------------------------------------------------------------------------------------------

Note to self in with weird windows magic.. SSH is managed by following directories in each respecitve CLI.

