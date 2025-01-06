import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the dataset
df = pd.read_csv('london_weather.csv')

# Check the first few rows
print(df.head())

# Convert the date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract year and month from the date
df['Year'] = df['date'].dt.year
df['Month'] = df['date'].dt.month

# Drop the 'date' column only if it exists
if 'date' in df.columns:
    df = df.drop(columns=['date'])

# Fill missing values with 0 for all columns
df = df.fillna(0)

#print(df.isnull().sum()) checking number of missing values in each column

# Features (excluding the target variable)
X = df[['cloud_cover', 'sunshine', 'global_radiation', 'pressure', 'snow_depth', 'Year', 'Month']]
# Target variable (let's predict the mean temperature, but you can change it to max_temp or min_temp)
y = df['mean_temp']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Random Forest model
model = RandomForestRegressor()
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')



