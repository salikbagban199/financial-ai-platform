import joblib
import pandas as pd

# Load the trained model
model = joblib.load("models/stock_model.pkl")

# Read stock data
df = pd.read_csv("data/apple_stock.csv", skiprows=2)

# Rename columns
df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

# Find the next day number
next_day = len(df) + 1

# Predict the next closing price
prediction = model.predict([[next_day]])

print("\n========== Prediction ==========")
print(f"Next Day Number : {next_day}")
print(f"Predicted Closing Price : ${prediction[0]:.2f}")