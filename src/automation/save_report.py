import pandas as pd

df = pd.read_csv("data/apple_stock.csv", skiprows=2)

df.columns = ["Date","Close","High","Low","Open","Volume"]

df["Close"] = pd.to_numeric(df["Close"])

highest = df["Close"].max()
lowest = df["Close"].min()
average = df["Close"].mean()

report = f"""
Financial AI Platform Report

Highest Price : {highest:.2f}

Lowest Price : {lowest:.2f}

Average Price : {average:.2f}
"""

with open("reports/stock_report.txt","w") as file:
    file.write(report)

print("✅ Report Saved")