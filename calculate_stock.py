def percentage_difference_series(series):
    return ((series.iloc[-1] - series.iloc[0]) / series.iloc[0]) * 100


def percentage_difference_df(df):
    end_price = df['close'].iloc[-1]
    start_price = df['close'].iloc[0]
    return ((end_price - start_price) / start_price) * 100
