import pandas as pd  # pandas library to work with tables of data


def top_3_categories(df):
    return (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )


def revenue_by_month(df):  
    # function that returns total revenue for each month
    df = df.copy()  # make a copy so the original data is not changed
    df["date"] = pd.to_datetime(df["date"])  # change the date text into real dates
    df["month"] = df["date"].dt.to_period("M")  # get year and month from each date, e.g. 2024-04
    return (  # send back the result
        df.groupby("month")["revenue"]  # put all orders from the same month together
        .sum()  # add up the revenue for each month
        .sort_index()  # sort from the earliest month to the latest
    )

def average_order_value(df):
    # Function that calculates the average revenue per order
    total_revenue = df["revenue"] .sum() # Calculate total revenue
    number_of_orders = df["order_id"] .nunique() #  Count unique orders
    if number_of_orders == 0: 
        return 0   # Avoid division by zero
    return total_revenue / number_of_orders  # Calculate AOV

def revenue_by_category(df):
    # Group all rows by product category
    # and calculate the total revenue for each category.
    result = (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    # Return the result containing all categories and thir revenue

    return result