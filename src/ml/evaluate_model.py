import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Read stock data
df = pd.read_csv("data/apple_stock.csv", skiprows=2)

# Rename columns
df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

# Convert Close column
df["Close"] = pd.to_numeric(df["Close"])

# Create Day column
df["Day"] = range(1, len(df) + 1)

# Input and Output
X = df[["Day"]]
y = df["Close"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Plot Actual vs Predicted
plt.figure(figsize=(8,5))

plt.scatter(X_test, y_test, label="Actual Price")

plt.scatter(X_test, predictions, label="Predicted Price")

plt.title("Actual vs Predicted Stock Price")

plt.xlabel("Day")

plt.ylabel("Closing Price")

plt.legend()

plt.grid(True)
print("\nActual Prices")
print(y_test.values)

print("\nPredicted Prices")
print(predictions)
plt.show()