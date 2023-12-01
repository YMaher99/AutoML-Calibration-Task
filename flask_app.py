import numpy as np
from flask import Flask, request, jsonify, abort
import pandas as pd
from joblib import load

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Get data from the POST request
        skewness = data.get('skewness')
        curtosis = data.get('curtosis')
        entropy = data.get('entropy')
        df = pd.DataFrame({'skewness':[skewness],'curtosis':[curtosis],'entropy':[entropy]})
        model = load(f"models/calibrated_classifier.joblib")
        prediction = float(model.predict_proba(df)[0][1])

    except Exception as e:
        print(e)
        abort(404, description=f"Invalid JSON body.\nPlease send a JSON body with a float value for skewness, curtosis, and entropy.")





    # Return the predicted value as JSON
    return jsonify({'output': prediction})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
