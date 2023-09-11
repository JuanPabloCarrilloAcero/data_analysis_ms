import os
import requests

STOCKS_MS_URL = os.getenv('STOCKS_MS_URL')
print(STOCKS_MS_URL)


# Function to get TIME_SERIES_DAILY from the stock API
# Takes in the stock API URL, API key, and the stock symbol
# Returns the JSON data from the API
def get_daily_data(symbol):
    try:
        response = requests.get(
            f"{STOCKS_MS_URL}/get/historic/{symbol}"
        )

        if response.status_code == 200:
            stock_data = response.json()
            return stock_data
        else:
            raise Exception("Failed to fetch data from the API")

    except Exception as e:
        raise e


def get_all_stocks():
    try:
        response = requests.get(
            f"{STOCKS_MS_URL}/get/empresas"
        )

        if response.status_code == 200:
            stock_data = response.json()
            return stock_data
        else:
            raise Exception("Failed to fetch data from the API")

    except Exception as e:
        raise e
    # return {"stocks": ["AAPL", "GOOG", "TSLA", "NVDA"]}
