# Median and Average Earnings grow with more Education

## Aaron Miller -  CS 416 Data Visualization - Dashboard Project - Professor John C. Hart - Summer 2025

---------------------------------------------------------------------------------------------------------------------

## Table 1: `wrangled_FRED_ca_county_education.csv` - *Wrangled and created by `mine_FRED.py`*

### Source: *FRED - Federal Reserve Bank of St. Louis* data

Data sets were gathered and wrangled from years 2010 to 2023. Below shows the approach used to create Table 1: `wrangled_FRED_ca_county_education.csv`.

1. [Bachelor's Degree or Higher (5-year estimate) by California County](https://fred.stlouisfed.org/release/tables?rid=330&eid=391686) 
2. Copied Data into Excel (`FRED\CA_Education_by_County_over_Years.xlsx`)
3. mine_FRED.py runs validations on Excel file from step 2, wrangles and creates the final table Table 1: `wrangled_FRED_ca_county_education.csv`

Attributes found in  Table 1: `wrangled_FRED_ca_county_education.csv`
**County:** CA Counties
**Percent:** Percent of population that recieved a bachelors degree or higher.
**Year:** The year the data was gathered for that record

---------------------------------------------------------------------------------------------------------------------

## Table 2: `wrangled_DataUSA_ca_county_housing.csv` - *Wrangled created by `mine_DataUSA.py`*

### Source: *Data USA* data

Data sets were gathered and wrangled for years 2013 to 2023 from Data USA.

<https://datausa.io/profile/geo/california#housing> &rarr; Download CSV &rarr;

This will lead you to --> <https://datausa.io/api/data?Geography=04000US06:children&measure=Household%20Income%20by%20Race,Household%20Income%20by%20Race%20Moe&drilldowns=Race>

Thi

---------------------------------------------------------------------------------------------------------------------

## Table 3 - Created by  `mine_BLS_FCC.py`

## Source:  *Bureau of Labor Statistics* mapped with *Federal Communication Commission* data

California County names from the Federal Communication Commision names were mapped to FIPs Bureau of Labor Statistics data

Source: <https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt>

The following data is from the Bureau of Labor Statistics

Source: <https://www.bls.gov/cew/downloadable-data-files.htm> &rarr; QCEW NAICS-Based Data Files (1975 - most recent) &rarr; Annual Averages

#### Bureau of Labor Statistics data columns derived from these [Definitions](https://www.bls.gov/cew/about-data/downloadable-file-layouts/annual/naics-based-annual-layout.htm)

| Column Name | Data Type Info | Explanation |
| :------- | :------ | :--- |
| **area_fips**| Numeric | This refers to the geographic location. I have only kept California county FIPs codes 06001 to 06115. |
| **own_code**| Numeric | 0 covers ownership for all Private,International Government,Local Government,State Government,Federal Government,Total Government,Total U.I. Covered |
| **industry_code**| 10|total of all QCEW Ownership Codes for NAICS Coded Data |
| **agglvl_code**|  10|  total of all QCEW Aggregation Level Codes (a) for NAICS Coded Data |
| **size_code**|  0 or blank| All establishment sizes |
| **year**|  2009-2023|  this is respective of each year we are mining the data for- capped at year 2009 due to <https://www.fhfa.gov/data/pudb> having started recording this|
|**annual_avg_emplvl** | *Numeric 9*| Annual average of monthly employment levels for a given year|
|**total_annual_wages** | *Numeric 15* | Sum of the four quarterly total wage levels for a given year |
|**taxable_annual_wages** | *Numeric 15* | Sum of the four quarterly total taxable wage totals for a given year |
|**annual_contributions** | *Numeric 13* | Sum of the four quarterly contribution totals for a given year |
|**annual_avg_wkly_wage** | *Numeric 8* | Average weekly wage based on the 12-monthly employment levels and total annual wage levels. |
|**avg_annual_pay** | *Numeric 8* | Average annual pay based on employment and wage levels for a given year. |
|**oty_total_annual_wages_chg** | *Numeric 15* | Over-the-year change in the total annual wages for a given year |
|**oty_total_annual_wages_pct_chg** | *Numeric 8* | Over-the-year percent change in total annual wages for a given year (Rounded to the tenths place) |
|**oty_taxable_annual_wages_chg** |*Numeric 15* |Over-the-year change in taxable annual wages for a given year |
|**oty_taxable_annual_wages_pct_chg**| *Numeric 8* |Over-the-year percent change in taxable annual wages for a given year (Rounded to the tenths place)|

----------------------------------------------------------------------------------------------------------------------------

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
