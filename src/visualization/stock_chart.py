import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("data/apple_stock.csv", skiprows=2)

# Rename columns
df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Convert Close column to number
df["Close"] = pd.to_numeric(df["Close"])

# Create graph
plt.figure(figsize=(10, 5))

plt.plot(df["Date"], df["Close"])

plt.title("Apple Stock Closing Price")
plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.grid(True)

plt.show()