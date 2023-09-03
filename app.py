import os

from flask import Flask, jsonify
from dotenv import load_dotenv

from get_stock_data import get_daily_data
from predict_price import predict_price
from transform_data import transform_daily

load_dotenv()

ALPHA_VANTAGE_KEY = os.environ.get('ALPHA_VANTAGE_KEY')
STOCK_API_URL = os.environ.get('STOCK_API_URL')

app = Flask(__name__)


# Main page controller
# returns a hello world message
@app.route('/')
def hello_world():
    return 'Hello World!'


# Price prediction controller
# takes in a symbol and a time
# returns the time series data
@app.route('/price_prediction/<symbol>/<time>', methods=['GET'])
def price_prediction(symbol, time):
    try:
        data = get_daily_data(STOCK_API_URL, ALPHA_VANTAGE_KEY, symbol)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    df = transform_daily(data)

    prediction = predict_price(df, time)

    print(prediction)

    return jsonify("all good"), 200


@app.route('/daily_data/<symbol>', methods=['GET'])
def daily_data(symbol):
    data = daily_data(STOCK_API_URL, ALPHA_VANTAGE_KEY, symbol)
    return data


# Valuable stock controller
# returns a list of valuable stocks based on future predictions
@app.route('/valuable_stock', methods=['GET'])
def valuable_stock():
    return 'Hello World!'


# Relevant stock controller
# returns a list of relevant stocks based on current values
@app.route('/relevant_stock', methods=['GET'])
def relevant_stock():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
