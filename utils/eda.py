
import pandas as pd
import matplotlib.pyplot as plt

# Load the weather data
df = pd.read_csv("data/weather_data.csv")

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

# Graph 4: Temperature for the first day
df_day1 = df[df["date"] < "2016-01-02"]

plt.figure(figsize=(10, 5))
plt.plot(df_day1["date"], df_day1["temperature_2m"])
plt.title("Temperature for the First Day")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.tight_layout()
plt.savefig("data/first_day_temperature.png")
plt.close()

# Graph 5: Temperature for the first week
df_week1 = df[df["date"] < "2016-01-08"]

plt.figure(figsize=(10, 5))
plt.plot(df_week1["date"], df_week1["temperature_2m"])
plt.title("Temperature for the First Week")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.tight_layout()
plt.savefig("data/first_week_temperature.png")
plt.close()


# Graph 6: Temperature for the first month
df_month1 = df[df["date"] < "2016-02-01"]

plt.figure(figsize=(10, 5))
plt.plot(df_month1["date"], df_month1["temperature_2m"])
plt.title("Temperature for the First Month")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.tight_layout()
plt.savefig("data/first_month_temperature.png")
plt.close()



print("All six graphs saved successfully!")
