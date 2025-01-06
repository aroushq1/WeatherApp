from flask import Flask, request, render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Load and preprocess data (same as before)
df = pd.read_csv('london_weather.csv')
df['date'] = pd.to_datetime(df['date'])
df['Year'] = df['date'].dt.year
df['Month'] = df['date'].dt.month
df = df.drop(columns=['date'])
df = df.dropna()

X = df[['cloud_cover', 'sunshine', 'global_radiation', 'pressure', 'snow_depth', 'Year', 'Month']]
y = df['mean_temp']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = RandomForestRegressor()
model.fit(X_scaled, y)

# Initialize Flask app
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    cloud_cover = float(request.form['cloud_cover'])
    sunshine = float(request.form['sunshine'])
    global_radiation = float(request.form['global_radiation'])
    pressure = float(request.form['pressure'])
    snow_depth = float(request.form['snow_depth'])
    year = int(request.form['year'])
    month = int(request.form['month'])
    
    # Process the input
    input_data = {
        'cloud_cover': [cloud_cover],
        'sunshine': [sunshine],
        'global_radiation': [global_radiation],
        'pressure': [pressure],
        'snow_depth': [snow_depth],
        'Year': [year],
        'Month': [month]
    }
    
    input_df = pd.DataFrame(input_data)
    input_scaled = scaler.transform(input_df)

    # Make prediction
    predicted_temp = model.predict(input_scaled)
    return render_template('index.html', prediction_text=f'Predicted Temperature: {predicted_temp[0]:.2f}°C')

if __name__ == "__main__":
    app.run(debug=True)
