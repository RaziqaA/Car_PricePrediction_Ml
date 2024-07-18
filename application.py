from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__, template_folder='Templates')

# Paths
model_path = "LinearRegressionModel.pkl"
data_path = 'Cleaned_Car_data.csv'

try:
    # Check if model file exists
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    # Load model
    model = pickle.load(open(model_path, 'rb'))
    logging.info("Model loaded successfully")

    # Check if data file exists
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found: {data_path}")

    # Load data
    car = pd.read_csv(data_path)
    logging.info("Data loaded successfully")

except Exception as e:
    logging.error(f"An error occurred: {e}")

@app.route('/')
def index():
    try:
        companies = sorted(car['company'].unique())
        car_models = sorted(car['name'].unique())
        years = sorted(car['year'].unique(), reverse=True)
        fuel_type = car['fuel_type'].unique()
        return render_template('index.html', companies=companies, car_models=car_models, years=years,
                               fuel_type=fuel_type)
    except Exception as e:
        logging.error(f"An error occurred in index route: {e}")
        return "An error occurred while loading the index page."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        company = request.form.get('Company')
        car_model = request.form.get('car_model')
        year = request.form.get('year')
        fuel_type = request.form.get('fuel_type')
        kms_driven = request.form.get('kms_driven')

        # DataFrame construction for prediction
        data = pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]],
                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
        prediction = model.predict(data)

        # Logging instead of print statements
        logging.info(f"Company: {company}, Car Model: {car_model}, Year: {year}, Fuel Type: {fuel_type}, Kms Driven: {kms_driven}")
        logging.info(f"Prediction: {prediction[0]}")

        return str(np.round(prediction[0], 3))
    except Exception as e:
        logging.error(f"An error occurred in predict route: {e}")
        return "An error occurred while making the prediction."

if __name__ == '__main__':
    app.run(debug=True)
