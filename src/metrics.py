import pandas as pd

def top_3_categories(df):
    return (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )

def total_revenue(df):
    return df["revenue"].sum()

def total_units(df):
    return df["units"].sum()

# (Funktionen är kopierad från Lavinas kod på GitHub 
# för att kunna skapa månadsdiagrammet i viz.py och report.ipynb.
# Kontrollera om funktionen redan finns i main för att undvika dubbletter/fler konflitter)

def revenue_by_month(df):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    return (
        df.groupby("month")["revenue"]
        .sum()
        .sort_index()
    )