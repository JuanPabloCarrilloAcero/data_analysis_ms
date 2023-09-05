from statsmodels.tsa.holtwinters import ExponentialSmoothing


# Function to predict the price of a stock
# Takes in the dataframe with daily data and the time
# Returns the predicted price
def predict_price(df, time):
    daily_data = df.resample('D').last()

    daily_data = daily_data.ffill()

    daily_data = daily_data.asfreq('D')

    daily_data['5D_MA'] = daily_data['Close'].rolling(window=5).mean()

    daily_data['20D_MA'] = daily_data['Close'].rolling(window=20).mean()

    model = ExponentialSmoothing(daily_data['Close'], trend='add', seasonal='add', seasonal_periods=30)
    model_fit = model.fit()

    one_month_predictions = model_fit.forecast(steps=time)

    return one_month_predictions
