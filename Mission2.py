from flask import Flask, jsonify, json, request
from flask_cors import CORS
from statsmodels.tsa.statespace.sarimax import SARIMAXResults


# Instantiate the app
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['POST'])
def index():
    """ function recieves post request containing 
        month and year values, and calls the forecast_value
        function to get prediction.

    Returns:
        json: {"prediction": value}
    """
    if not request.json:
        abort(400)
    
    req = request.json 
    prediction = forecast_value(req['month'], req['year'])
    return jsonify({"prediction": prediction})


def forecast_value(month, year):
    """ this function loads saved model from pickle file
        and creates the proper time date formate to be 
        fed to the model.
    
    Args:
        month (int): month indication
        year (int): year indication

    Returns:
        int: predicted value
    """
    date = str(year) + '-' + str("%02d" % month) + '-' + '01'
    load_model = SARIMAXResults.load("accident_model.pickle")
    result = int(load_model.predict(date, date))
    
    return result


if __name__ == '__main__':
    app.run()
