# E-handel-repo
Data Loading and Exploration
- Created a function to load the CSV file using pandas.
- Checked data types, missing values, and duplicate rows.
- Converted the date column to datetime format and checked the date range, total rows, and unique orders.
Revenue Analysis
- Added a function to display the top 3 categories by revenue.
- Added a function to calculate total revenue by month.

How the monthly revenue is calculated (`revenue_by_month` in `src/metrics.py`):
1. Make a copy of the data so the original DataFrame is not changed.
2. Convert the `date` column to datetime format, so we can read the month from each date.
3. Create a `month` column from each date (e.g. 2024-04-19 becomes 2024-04). The year is kept, so January 2024 and January 2025 are counted as different months.
4. Group the orders by month and add up the `revenue` column for each month.
5. Sort the result from the earliest month to the latest.

Result (January to June 2024):

| Month   | Revenue    |
|---------|------------|
| 2024-01 | 664,083.32 |
| 2024-02 | 548,462.03 |
| 2024-03 | 487,602.00 |
| 2024-04 | 580,194.83 |
| 2024-05 | 632,165.16 |
| 2024-06 | 590,259.89 |

Total revenue for the period: 3,502,767.23. January had the highest revenue and March the lowest.
