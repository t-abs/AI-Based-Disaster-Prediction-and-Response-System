from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and feature list
model = joblib.load("random_forest_model.pkl")
model_features = joblib.load("model_features.pkl")

# Input fields based on user-provided data
original_input_features = [
    'Latitude',
    'Longitude',
    'Rainfall (mm)',
    'Temperature (°C)',
    'Humidity (%)',
    'River Discharge (m³/s)',
    'Water Level (m)',
    'Elevation (m)',
    'Land Cover',
    'Soil Type',
    'Population Density',
    'Infrastructure',
    'Historical Floods'
]

@app.route('/')
def index():
    return render_template("index.html", input_features=original_input_features)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = {key: request.form[key] for key in request.form}

    # Convert numeric values where possible
    for key in input_data:
        try:
            input_data[key] = float(input_data[key])
        except:
            pass  # For categorical fields like "Land Cover", etc.

    input_df = pd.DataFrame([input_data])

    # One-hot encode and align with training features
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=model_features, fill_value=0)

    # Predict
    prediction = model.predict(input_df)[0]
    result = "Yes" if prediction == 1 else "No"

    return render_template("index.html", prediction=result, input_features=original_input_features)

if __name__ == '__main__':
    app.run(debug=True)
