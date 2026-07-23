import pandas as pd

# Read stock data
df = pd.read_csv("data/apple_stock.csv", skiprows=2)

# Rename columns
df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

# Convert numeric columns
for col in ["Close", "High", "Low", "Open", "Volume"]:
    df[col] = pd.to_numeric(df[col])

# Calculate values
current = df["Close"].iloc[-1]
highest = df["Close"].max()
lowest = df["Close"].min()
average = df["Close"].mean()
total_volume = df["Volume"].sum()

# Create results table
results = pd.DataFrame({
    "Metric": [
        "Current Price",
        "Highest Price",
        "Lowest Price",
        "Average Price",
        "Total Volume"
    ],
    "Value": [
        current,
        highest,
        lowest,
        round(average, 2),
        total_volume
    ]
})

# Save CSV
results.to_csv("reports/results.csv", index=False)

print("✅ Results exported successfully!")