import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/air_quality.csv")

print("Columns:", df.columns.tolist())
print(df.head())

df['datetime'] = pd.to_datetime(df['Data'], dayfirst=True, errors='coerce')

# Daily averages
daily = df.groupby(df['datetime'].dt.date)['Valore'].mean()
plt.figure(figsize=(12,6))
daily.plot(title="Daily Average Air Quality (All Sensors)")
plt.ylabel("Value")
plt.xlabel("Date")
plt.savefig("../figures/daily_average.png", dpi=150, bbox_inches="tight")

# Monthly averages
df['month'] = df['datetime'].dt.month
monthly = df.groupby('month')['Valore'].mean()
plt.figure(figsize=(10,6))
monthly.plot(kind="bar", title="Average Monthly Values (All Sensors)")
plt.ylabel("Value")
plt.xlabel("Month")
plt.savefig("../figures/monthly_average.png", dpi=150, bbox_inches="tight")

# Distribution of values
plt.figure(figsize=(10,6))
df['Valore'].plot(kind="hist", bins=30, title="Distribution of Sensor Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("../figures/value_distribution.png", dpi=150, bbox_inches="tight")

print("✅ Figures saved in the 'figures/' folder")

