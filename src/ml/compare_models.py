import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Read data
df = pd.read_csv("data/apple_stock.csv", skiprows=2)

df.columns = ["Date","Close","High","Low","Open","Volume"]

# Convert numeric columns
for col in ["Close","High","Low","Open","Volume"]:
    df[col] = pd.to_numeric(df[col])

# Features
X = df[["Open","High","Low","Volume"]]

# Target
y = df["Close"]

# Split data
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train,y_train)

lr_prediction = lr.predict(X_test)

# Decision Tree
tree = DecisionTreeRegressor(random_state=42)

tree.fit(X_train,y_train)

tree_prediction = tree.predict(X_test)

# Accuracy
lr_score = r2_score(y_test,lr_prediction)
tree_score = r2_score(y_test,tree_prediction)

print("\n===== Model Comparison =====")

print(f"Linear Regression Score : {lr_score:.2f}")

print(f"Decision Tree Score     : {tree_score:.2f}")

if lr_score > tree_score:
    print("\n🏆 Best Model : Linear Regression")
else:
    print("\n🏆 Best Model : Decision Tree")