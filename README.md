# Median and Average Earnings grow with more Education

## Aaron Miller -  CS 416 Data Visualization - Dashboard Project - Summer 2025 - Professor John C. Hart


---------------------------------------------------------------------------------------------------------------------

I can make income and education  quartiles

``` Tableau
IF [Year] = 2013 THEN
    IF [Percent of Adults with Bachelors or Higher] > 21.70 THEN "Upper Half of Bachelor/Higher Education"
    ELSE "Lower Half of Bachelor/Higher Education"
    END
ELSEIF [Year] = 2014 THEN
    IF [Percent of Adults with Bachelors or Higher] > 22.45 THEN "Upper Half of Bachelor/Higher Education"
    ELSE "Lower Half of Bachelor/Higher Education"
    END
ELSEIF [Year] = 2015 THEN
    IF [Percent of Adults with Bachelors or Higher] > 22.40 THEN "Upper Half of Bachelor/Higher Education"
    ELSE "Lower Half of Bachelor/Higher Education"
    END
ELSEIF [Year] = 2016 THEN
    IF [Percent of Adults with Bachelors or Higher] > 22.40 THEN "Upper Half of Bachelor/Higher Education"
    ELSE "Lower Half of Bachelor/Higher Education"
    END
ELSEIF [Year] = 2017 THEN
    IF [Percent of Adults with Bachelors or Higher] > 23.30 THEN "Upper Half of Bachelor/Higher Education"
    ELSE "Lower Half of Bachelor/Higher Education"
    END
ELSEIF [Year] = 2018 THEN
    IF [Percent of Adults with Bachelors or Higher] > 23.45 THEN "Upper Half of Bachelor/Higher Education"
    ELSE "Lower Half of Bachelor/Higher Education"
    END
ELSEIF [Year] = 2019 THEN
    IF [Percent of Adults with Bachelors or Higher] > 24.05 THEN "Upper Half of Bachelor/Higher Education"
    ELSE "Lower Half of Bachelor/Higher Education"
    END
ELSEIF [Year] = 2020 THEN
    IF [Percent of Adults with Bachelors or Higher] > 24.25 THEN "Upper Half of Bachelor/Higher Education"
    ELSE "Lower Half of Bachelor/Higher Education"
    END
ELSEIF [Year] = 2021 THEN
    IF [Percent of Adults with Bachelors or Higher] > 24.55 THEN "Upper Half of Bachelor/Higher Education"
    ELSE "Lower Half of Bachelor/Higher Education"
    END
ELSEIF [Year] = 2022 THEN
    IF [Percent of Adults with Bachelors or Higher] > 24.25 THEN "Upper Half of Bachelor/Higher Education"
    ELSE "Lower Half of Bachelor/Higher Education"
    END
ELSEIF [Year] = 2023 THEN
    IF [Percent of Adults with Bachelors or Higher] > 25.00 THEN "Upper Half of Bachelor/Higher Education"
    ELSE "Lower Half of Bachelor/Higher Education"
    END
ELSE
    IF [Percent of Adults with Bachelors or Higher] > 23.65 THEN "Upper Half of the pain in my @"
    ELSE "What a pain"
    END
END
```

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
|**area_fips**| This refers to the geographic location. I have only kept California county FIPs codes 06001 to 06115. |
|**County**| Any of the 58 Counties in California|
|**own_code**| 0 covers ownership for all Private,International Government,Local Government,State Government,Federal Government,Total Government,Total U.I. Covered |
|**industry_code**| total of all QCEW Ownership Codes for NAICS Coded Data |
|**agglvl_code**| total of all QCEW Aggregation Level Codes (a) for NAICS Coded Data - 70 = County, Total Covered |
|**size_code**| 0 represents all establishment sizes |
|**year**| this is respective of each year we are mining the data for- capped at year 2009 due to <https://www.fhfa.gov/data/pudb> having started recording this|
|**annual_avg_emplvl**|  Annual average of monthly employment levels for a given year. This represents the average number of workers in the county.|
|**total_annual_wages**| Sum of the four quarterly total wage levels for a given year |
|**taxable_annual_wages**| Sum of the four quarterly total taxable wage totals for a given year |
|**annual_contributions**| Sum of the four quarterly contribution totals for a given year |
|**annual_avg_wkly_wage**| Average weekly wage based on the 12-monthly employment levels and total annual wage levels. |
|**avg_annual_pay**|  Average annual pay based on employment and wage levels for a given year. |
|**oty_total_annual_wages_chg**|  Over-the-year change in the total annual wages for a given year |
|**oty_total_annual_wages_pct_chg**| Over-the-year percent change in total annual wages for a given year (Rounded to the tenths place) |
|**oty_taxable_annual_wages_chg**| Over-the-year change in taxable annual wages for a given year |
|**oty_taxable_annual_wages_pct_chg**| Over-the-year percent change in taxable annual wages for a given year (Rounded to the tenths place)|
|**Annual_Wage_Quartiles_by_each_Year**| For each year every County is assigned a respective quartile by on avg_annual_pay|

---------------------------------------------------------------------------------------------------------------------

## Other Sources

Federal Communication Commission: <https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt>

--------------------------------------------------------------------------------------------------------------------

## Dashboard Evaluation and Questions

[10] Providing a proper URL to the dashboard, and the dashboard appears at that URL without any further user intervention.

[30] What is one question that the dashboard can answer by utilizing two or more simultaneously displayed charts? What is the answer? How do these two charts indicate the answer? (Spend some time to make sure you have picked a question whose answer is not simply given by just one of the charts, and the combination of the two charts gives a complete answer.)

```txt
Does having a larger percentage of a Bachelors degree or higher education lead to larger median and average earnings for Counties in California? Yes we can see that there is a strong collelation with higher earnings for areas that have a higher percentage of the population that has a Bacherlors degree or higher.
```

[10] Upload a screenshot of your dashboard answering that question by showing two or more simultaneously displayed charts.

[20] How does the layout of these charts promote visual understanding of the data across multiple charts? Do the charts follow a consistent color scheme and are they well aligned with each other to promote better visual comparisons.

[10] Indicate which chart should be graded as a "first" chart. Then justify the choice of this chart type, its axes and marks based on the data variables it shows.

[10] Indicate which chart should be graded as a "second" chart. Then justify the choice of this chart type, its axes and marks based on the data variables it shows.

[10] How does your dashboard provide details on demand?

[10] How does your dashboard support cross-filtering between these two charts?  (Required for 4 credit hour students. Optional extra credit for 3 credit hour students.)

----------------------------------------------------------------------------------------------------------------------------------------
Note to self in , SSH is managed by

```
WSL - /home/aarje/.ssh 
CMD - C:\Users\Aarje\.ssh
PS1 - C:\Users\Aarje\.ssh
```

uhhh
