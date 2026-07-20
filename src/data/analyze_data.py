import pandas as pd

# Read CSV and skip the extra rows
df = pd.read_csv("data/apple_stock.csv", skiprows=2)

# Rename the columns
df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

# Convert columns to numbers
df["Close"] = pd.to_numeric(df["Close"])
df["High"] = pd.to_numeric(df["High"])
df["Low"] = pd.to_numeric(df["Low"])
df["Open"] = pd.to_numeric(df["Open"])
df["Volume"] = pd.to_numeric(df["Volume"])

print("\n===== Apple Stock Analysis =====")

print("Highest Closing Price :", df["Close"].max())
print("Lowest Closing Price  :", df["Close"].min())
print("Average Closing Price :", round(df["Close"].mean(), 2))
print("Total Trading Volume  :", df["Volume"].sum())