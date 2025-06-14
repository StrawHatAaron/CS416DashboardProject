# Median and Average Earnings grow with Education

## Aaron Miller -  CS 416 Data Visualization - Dashboard Project - Professor John C. Hart - Summer 2025 

---------------------------------------------------------------------------------------------------------------------

## Table 1 - Created by `mine_DataUSA.py`

### *Data USA* data

<https://datausa.io/profile/geo/california#housing> &rarr; Download CSV &rarr;

This will lead you to --> <https://datausa.io/api/data?Geography=04000US06:children&measure=Household%20Income%20by%20Race,Household%20Income%20by%20Race%20Moe&drilldowns=Race>

Thi

---------------------------------------------------------------------------------------------------------------------

## Table 2 - Created by  `mine_BLS_FCC.py`

## *Bureau of Labor Statistics* mapped with *Federal Communication Commission* data

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

 Over recent time has the stagnation of wages led to 
   1. can compare median earning vs average earnings and show localized wealth gaps over time through the increase of average wages**** I like this alot with the new file 
   2. higher levels of foreclosure on mortgages purchased by each Federal Home Loan Banks?

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
