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
