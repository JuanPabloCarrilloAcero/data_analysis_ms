from dotenv import load_dotenv
from flask import Flask, jsonify

from services import price_prediction_service, valuable_stock_service

load_dotenv()

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
        result = price_prediction_service(symbol, time).to_json()
        return result, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Valuable stock controller
# returns a list of valuable stocks based on future predictions
@app.route('/valuable_stock/<time>', methods=['GET'])
def valuable_stock(time):
    try:
        result = valuable_stock_service(time)
        return result, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Relevant stock controller
# returns a list of relevant stocks based on current values
@app.route('/relevant_stock/<time>', methods=['GET'])
def relevant_stock(time):
    try:
        result = relevant_stock_service(time)
        return result, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run()
