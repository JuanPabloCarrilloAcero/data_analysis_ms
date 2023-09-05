import os
import requests

ALPHA_VANTAGE_KEY = os.environ.get('ALPHA_VANTAGE_KEY')
STOCK_API_URL = os.environ.get('STOCK_API_URL')


# Function to get TIME_SERIES_DAILY from the stock API
# Takes in the stock API URL, API key, and the stock symbol
# Returns the JSON data from the API
def get_daily_data(symbol):
    try:
        response = requests.get(
            f"{STOCK_API_URL}/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_KEY}"
        )

        if response.status_code == 200:
            stock_data = response.json()
            return stock_data
        else:
            raise Exception("Failed to fetch data from the API")

    except Exception as e:
        raise e


def get_all_stocks():
    return {"stocks": ["AAPL", "GOOG", "TSLA", "NVDA"]}
