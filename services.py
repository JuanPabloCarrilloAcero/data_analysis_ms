from calculate_stock import percentage_difference_series, percentage_difference_df
from get_stock_data import get_daily_data, get_all_stocks
from predict_price import predict_price
from transform_data import transform_daily
from transform_data import transform_stocks


def price_prediction_service(symbol, time):
    try:
        time = int(time)
    except Exception:
        raise Exception("time must be an integer")

    try:
        data = get_daily_data(symbol)
    except Exception as e:
        raise e

    df = transform_daily(data)

    prediction = predict_price(df, time)

    return prediction


def valuable_stock_service(time):
    try:
        time = int(time)
    except Exception:
        raise Exception("time must be an integer")

    try:
        stocks = get_all_stocks()
    except Exception:
        raise Exception("failed to get all stocks")

    stocks = transform_stocks(stocks)

    results = []

    for stock in stocks:
        try:
            prediction = price_prediction_service(stock['ticker'], time)
        except Exception:
            raise Exception(f"failed to get prediction for {stock}")
        percentage_difference = percentage_difference_series(prediction)
        results.append({"symbol": stock['ticker'], "percentage_difference": percentage_difference})

    return results


def relevant_stock_service(time):
    try:
        time = int(time)
    except Exception:
        raise Exception("time must be an integer")

    try:
        stocks = get_all_stocks()
    except Exception:
        raise Exception("failed to get all stocks")

    stocks = transform_stocks(stocks)

    results = []

    for stock in stocks:
        try:
            data = get_daily_data(stock['ticker'])
        except Exception:
            raise Exception(f"failed to retrieve data from {stock}")

        df = transform_daily(data)

        percentage_difference = percentage_difference_df(df)
        results.append({"symbol": stock['ticker'], "percentage_difference": percentage_difference})

    return results
