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