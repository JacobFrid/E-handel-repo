def top_3_categories(df):
    return (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )
