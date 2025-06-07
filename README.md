--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

https://www.bls.gov/cew/downloadable-data-files.htm ---> QCEW NAICS-Based Data Files (1975 - most recent)

Don't need to be able to reach into every subset although it would be interesting, I need to target in the data the following:

****filter and yank****
area_fips	- all of them			- 	need all of these along with each record I will target, need to break up into FIPSStateNumericCode and FIPSCountyCode. Ex FIP=1000=01000=Aalabama
own_code	- 0				- 	0 covers ownership for all Private,International Government,Local Government,State Government,Federal Government,Total Government,Total U.I. Covered 
industry_code	- 10				-	total of all QCEW Ownership Codes for NAICS Coded Data
agglvl_code	- 10				-	total of all QCEW Aggregation Level Codes (a) for NAICS Coded Data
size_code	- 0 or blank			-	All establishment sizes
year		- 2009-2023			-	this is respective of each year we are mining the data for- capped at year 2009 due to https://www.fhfa.gov/data/pudb having started recording this 

****yank****
15	annual_avg_emplvl	Numeric	9	Annual average of monthly employment levels for a given year
16	total_annual_wages	Numeric	15	Sum of the four quarterly total wage levels for a given year
17	taxable_annual_wages	Numeric	15	Sum of the four quarterly total taxable wage totals for a given year
18	annual_contributions	Numeric	13	Sum of the four quarterly contribution totals for a given year
19	annual_avg_wkly_wage	Numeric	8	Average weekly wage based on the 12-monthly employment levels and total annual wage levels.
20	avg_annual_pay	Numeric	8	Average annual pay based on employment and wage levels for a given year.
34	oty_total_annual_wages_chg	Numeric	15	Over-the-year change in the total annual wages for a given year
35	oty_total_annual_wages_pct_chg	Numeric	8	Over-the-year percent change in total annual wages for a given year (Rounded to the tenths place)
36	oty_taxable_annual_wages_chg	Numeric	15	Over-the-year change in taxable annual wages for a given year
37	oty_taxable_annual_wages_pct_chg	Numeric	8	Over-the-year percent change in taxable annual wages for a given year (Rounded to the tenths place)

//industry_title- 10 Total, all industries	-	this refers to all the industries as a whole, industry_code=10 represents this too
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------








--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
https://www.fhfa.gov/data/pudb ---> https://www.fhfa.gov/document/ama_pudb_definitions_2023.pdf
Don't need to be able to reach into every subset although it would be interesting, I need to target in the data the following:
could use this data to say that due to wage stagnation homeowners are becoming older on average.


think I need to do this instead
https://www.fhfa.gov/data/national-mortgage-database-aggregate-statistics --> Res​idential Mort​gage Performance Statistics	




nope focusing on this one now
nmdb-new-mortgage-statistics-all-annual.csv




-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 





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