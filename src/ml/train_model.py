import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Read data
df = pd.read_csv("data/apple_stock.csv", skiprows=2)

# Rename columns
df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

# Convert Close to numeric
df["Close"] = pd.to_numeric(df["Close"])

# Create Day column
df["Day"] = range(1, len(df) + 1)

# Input and Output
X = df[["Day"]]
y = df["Close"]

# Split data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate Accuracy
mae = mean_absolute_error(y_test, predictions)
score = r2_score(y_test, predictions)

print("\n========== MODEL REPORT ==========")
print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")
print(f"Mean Absolute Error : {mae:.2f}")
print(f"R² Score : {score:.2f}")

# Save model
joblib.dump(model, "models/stock_model.pkl")

print("\n✅ Model trained and saved successfully!")