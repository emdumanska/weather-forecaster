
import pandas as pd
import matplotlib.pyplot as plt

# Load the weather data
df = pd.read_csv("data/weather.csv")

# Convert the date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Graph 1: Temperature over time
plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["temperature_2m"])
plt.title("Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.tight_layout()
plt.savefig("data/temperature_over_time.png")
plt.close()

# Graph 2: Average temperature by month
df["month"] = df["date"].dt.month
monthly_avg = df.groupby("month")["temperature_2m"].mean()

plt.figure(figsize=(10, 5))
monthly_avg.plot(kind="bar")
plt.title("Average Temperature by Month")
plt.xlabel("Month")
plt.ylabel("Average Temperature (C)")
plt.tight_layout()
plt.savefig("data/monthly_temperature.png")
plt.close()

# Graph 3: Temperature vs humidity
plt.figure(figsize=(10, 5))
plt.scatter(df["temperature_2m"], df["relative_humidity_2m"], alpha=0.1)
plt.title("Temperature vs Humidity")
plt.xlabel("Temperature (C)")
plt.ylabel("Relative Humidity (%)")
plt.tight_layout()
plt.savefig("data/temperature_vs_humidity.png")
plt.close()

print("All three graphs saved successfully!")
