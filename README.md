# London Weather Predictor

This web application predicts the average temperature in London based on several weather features such as cloud cover, sunshine hours, global radiation, pressure, snow depth, year, and month. It uses a machine learning model built with Random Forest regression to make predictions.

## Features

- **Weather Prediction**: Predict the average temperature for a given set of weather parameters.
- **Machine Learning Model**: Trains a Random Forest regressor using historical weather data.
- **Interactive Web Interface**: Built using Flask, allowing users to enter weather data and receive predictions.

## Project Structure

The project is structured as follows:

WeatherApp/ │ ├── app.py # Main Flask application script ├── model.py # Script to train the machine learning model ├── london_weather.csv # Dataset used for training the model ├── templates/ │ └── index.html # HTML template for the web interface └── static/ └── style.css # Custom CSS for the app's styling


## Dependencies

This project requires the following Python packages:

- Flask
- pandas
- scikit-learn
- matplotlib
- seaborn

You can install all the dependencies by running:

```bash
pip install -r requirements.txt

## How To Run the App

1. Clone this repository or download the files.

2. Navigate to the project directory in your terminal.

3. Ensure that you have the required Python packages installed by running:

pip install -r requirements.txt

Open your browser and visit http://127.0.0.1:5000/ to access the application


Apologies for the confusion! Here is the full README.md content that you can easily copy:

markdown
Copy code
# London Weather Predictor

This web application predicts the average temperature in London based on several weather features such as cloud cover, sunshine hours, global radiation, pressure, snow depth, year, and month. It uses a machine learning model built with Random Forest regression to make predictions.

## Features

- **Weather Prediction**: Predict the average temperature for a given set of weather parameters.
- **Machine Learning Model**: Trains a Random Forest regressor using historical weather data.
- **Interactive Web Interface**: Built using Flask, allowing users to enter weather data and receive predictions.

## Project Structure

The project is structured as follows:

WeatherApp/ │ ├── app.py # Main Flask application script ├── model.py # Script to train the machine learning model ├── london_weather.csv # Dataset used for training the model ├── templates/ │ └── index.html # HTML template for the web interface └── static/ └── style.css # Custom CSS for the app's styling

markdown
Copy code

## Dependencies

This project requires the following Python packages:

- Flask
- pandas
- scikit-learn
- matplotlib
- seaborn

You can install all the dependencies by running:

```bash
pip install -r requirements.txt
requirements.txt
To install the dependencies, create a requirements.txt file with the following contents:

##requirements.txt
To install the dependencies, create a requirements.txt file with the following contents:
Flask==2.0.2
pandas==1.3.3
scikit-learn==0.24.2
matplotlib==3.4.3
seaborn==0.11.2


# How to Run the App
Clone this repository or download the files.

Navigate to the project directory in your terminal.

Ensure that you have the required Python packages installed by running:

bash
Copy code
pip install -r requirements.txt
Run the Flask app by executing:

bash
Copy code
python app.py
Open your browser and visit http://127.0.0.1:5000/ to access the application.

# How the Model Works
Data Preprocessing:

The dataset is loaded from the london_weather.csv file.
Missing values are handled by dropping or filling them with appropriate values.

Date features are extracted into separate Year and Month columns.

Feature Selection:

The features used for prediction are cloud cover, sunshine, global radiation, pressure, snow depth, year, and month.

Model Training:

The data is split into training and test sets.
A Random Forest regressor model is trained using the training data.

Prediction:

After training, the model predicts the average temperature based on the input features from the user.

# How to Use the App
Navigate to the app in your browser.
Enter the weather parameters (cloud cover, sunshine hours, global radiation, pressure, snow depth, year, and month).
Click the "Predict Temperature" button.
The predicted temperature will be displayed below the form.


# License
This project is open-source and available under the MIT License.

# Acknowledgments
The weather data used in this project is based on historical weather data for London.

This project uses the Random Forest model from the scikit-learn library for prediction.


