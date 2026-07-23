import pandas as pd

# Read stock data
df = pd.read_csv("data/apple_stock.csv", skiprows=2)

# Rename columns
df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

# Convert Close column
df["Close"] = pd.to_numeric(df["Close"])

# Calculate values
current_price = df["Close"].iloc[-1]
highest_price = df["Close"].max()
lowest_price = df["Close"].min()
average_price = df["Close"].mean()                                      

# First and last price
first_price = df["Close"].iloc[0]
last_price = df["Close"].iloc[-1]

# -----------------------
# Market Trend
# -----------------------
difference = last_price - first_price

if difference > 2:
    trend = "📈 Uptrend"
elif difference < -2:
    trend = "📉 Downtrend"
else:
    trend = "➖ Sideways"

# -----------------------
# Recommendation
# -----------------------
if current_price > average_price:
    recommendation = "BUY"
elif current_price < average_price:
    recommendation = "SELL"
else:
    recommendation = "HOLD"

# -----------------------
# Risk Analysis
# -----------------------
price_difference = highest_price - lowest_price

if price_difference < 20:
    risk = "🟢 LOW RISK"
    risk_reason = "Price changes are small."

elif price_difference <= 50:
    risk = "🟡 MEDIUM RISK"
    risk_reason = "Price changes are moderate."

else:
    risk = "🔴 HIGH RISK"
    risk_reason = "Price changes are large."

# -----------------------
# AI Report
# -----------------------
report = f"""
=============================
      AI FINANCIAL REPORT
=============================

Current Price : ${current_price:.2f}

Highest Price : ${highest_price:.2f}

Lowest Price : ${lowest_price:.2f}

Average Price : ${average_price:.2f}

Market Trend : {trend}

Recommendation : {recommendation}

Risk Level : {risk}

Risk Reason : {risk_reason}

---------------------------------------

Summary

Apple stock traded between
${lowest_price:.2f} and ${highest_price:.2f}.

The average closing price was
${average_price:.2f}.

Current market trend is
{trend}.

Recommendation :
{recommendation}

Risk :
{risk}
"""

print(report)