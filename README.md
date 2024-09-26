

# Car Price Prediction Model

## Project Overview
This project aims to predict the prices of cars based on various parameters using a linear regression model. The model utilizes features such as the car's name, company, year of manufacture, price, kilometers driven, and fuel type to make accurate predictions. The model is integrated with a Flask web application that serves a user-friendly interface for making predictions.

## Table of Contents
1. [Dataset Information](#dataset-information)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Model Training](#model-training)
5. [Web Application](#web-application)
6. [License](#license)
7. [Acknowledgements](#acknowledgements)

## Dataset Information
The dataset consists of the following parameters:
- **Name**: The model name of the car.
- **Company**: The manufacturer of the car.
- **Year**: The year the car was manufactured.
- **Price**: The market price of the car.
- **Kms Driven**: Total kilometers driven by the car.
- **Fuel Type**: Type of fuel used (e.g., Petrol, Diesel, Electric).

## Installation
To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Car_PricePrediction_Ml
   ```
2. **Navigate to the project directory**:
   ```bash
   cd car-price-prediction
   ```
3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the application:

1. Ensure that you have the required packages installed.
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

### Making Predictions
- Input the required parameters (name, company, year, kms driven, fuel type) in the web form.
- Click on the "Predict" button to see the predicted price of the car.

## Model Training
The linear regression model is trained using the dataset. The following steps were followed:
1. Data preprocessing: Handling missing values and encoding categorical features.
2. Splitting the dataset into training and test sets.
3. Training the linear regression model on the training set.
4. Saving the trained model using Pickle for future predictions.

The Pickle file (`LinearRegressionModel.pkl`) is included in the project and is loaded by the Flask application to make predictions.

## Web Application
The web application is built using Flask and Jinja2 for templating. It provides a simple interface for users to input car parameters and receive price predictions.

### Directory Structure
```
car-price-prediction/
│
├── app.py               # Flask application
├── model.pkl            # Trained linear regression model
├── requirements.txt     # Required packages
├── templates/           # HTML templates for the frontend
│   └── index.html       # Main page for predictions
└── static/              # Static files (CSS, JS)
```

## License
This project is licensed under the MIT License.

## Acknowledgements
- The dataset used for training the model.
- Flask documentation for guidance on web development.




