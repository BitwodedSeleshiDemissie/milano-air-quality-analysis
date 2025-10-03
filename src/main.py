import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Load dataset
df = pd.read_csv("data/air_quality.csv")

# Parse datetime
df['datetime'] = pd.to_datetime(df['DATA'], errors='coerce')

# Filter for Milano
df_milano = df[df['NOME_COMUNE'] == 'MILANO']

# Aggregate daily average PM10
daily_pm10 = df_milano.groupby(df_milano['datetime'].dt.date)['PM10'].mean()

# Drop missing values
daily_pm10 = daily_pm10.dropna()

# Train ARIMA model
model = ARIMA(daily_pm10, order=(2,1,2))
model_fit = model.fit()

# Forecast next 7 days
forecast = model_fit.forecast(steps=7)
print("7-day forecast for PM10 in Milan (µg/m³):")
print(forecast)

