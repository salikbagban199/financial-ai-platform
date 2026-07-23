import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Read stock data
df = pd.read_csv("data/apple_stock.csv", skiprows=2)

# Rename columns
df.columns = ["Date","Close","High","Low","Open","Volume"]

# Convert numeric columns
columns = ["Close","High","Low","Open","Volume"]

for col in columns:
    df[col] = pd.to_numeric(df[col])

# Features
X = df[["Open","High","Low","Volume"]]

# Target
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

# Prediction
predictions = model.predict(X_test)

# Accuracy
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n===== Improved Model =====")
print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))
print("Mean Absolute Error :", round(mae,2))
print("R² Score :", round(r2,2))

# Save model
joblib.dump(model,"models/improved_stock_model.pkl")

print("\n✅ Improved model saved successfully!")