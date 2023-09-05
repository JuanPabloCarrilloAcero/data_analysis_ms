from get_stock_data import get_daily_data, get_all_stocks
from predict_price import predict_price
from transform_data import transform_daily


def price_prediction_service(symbol, time):
    try:
        time = int(time)
    except Exception as e:
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

    stocks = stocks['stocks']

    results = []

    for stock in stocks:
        try:
            prediction = price_prediction_service(stock, time)
        except Exception:
            raise Exception(f"failed to get prediction for {stock}")
        percentage_difference = ((prediction.iloc[-1] - prediction.iloc[0]) / prediction.iloc[0]) * 100
        results.append({"symbol": stock, "percentage_difference": percentage_difference})

    return results
