import pandas as pd


# Transform data from TIME_SERIES_DAILY JSON to a dataframe changing:
# - The column names to Open, High, Low, Close, Volume
# - The data types to float
# - The index to datetime
# - The NaN values to 0
def transform_daily(data_json):
    time_series_data = data_json["Time Series (Daily)"]

    df = pd.DataFrame(time_series_data).T

    df = df.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    })

    df[["Open", "High", "Low", "Close", "Volume"]] = df[["Open", "High", "Low", "Close", "Volume"]].astype(float)

    df.index = pd.to_datetime(df.index)

    df = df.dropna()

    return df
