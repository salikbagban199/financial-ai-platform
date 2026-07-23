import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf

# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(
    page_title="Financial AI Platform",
    page_icon="📈",
    layout="wide"
)

# --------------------------
# Sidebar
# --------------------------
st.sidebar.title("📂 Dashboard Menu")

stocks = {
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "Google": "GOOGL"
}

stock = st.sidebar.selectbox(
    "Select Stock",
    list(stocks.keys())
)

ticker = stocks[stock]

st.sidebar.success(f"Selected Stock: {stock}")

# --------------------------
# Dashboard Title
# --------------------------
st.title("📈 Financial AI Platform")

st.write("AI-powered Financial Data Analysis Dashboard")

st.markdown("---")

# Load Data

# Download live stock data
# Download live stock data
# Download live stock data
df = yf.download(
    ticker,
    period="1mo",
    progress=False
)

# Remove MultiIndex if present
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

# Keep required columns
df = df[["Open", "High", "Low", "Close", "Volume"]]

# Convert index into a normal column
df.reset_index(inplace=True)

# Rename the first column to Date
df.rename(columns={df.columns[0]: "Date"}, inplace=True)


# KPIs
current = float(df["Close"].iloc[-1])
highest = float(df["Close"].max())
lowest = float(df["Close"].min())
average = float(df["Close"].mean())
st.header("📊 Stock Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Current Price", f"${current:.2f}")
c2.metric("Highest Price", f"${highest:.2f}")
c3.metric("Lowest Price", f"${lowest:.2f}")
c4.metric("Average Price", f"${average:.2f}")

st.markdown("---")

# Closing Price Chart
st.header("📈 Closing Price")

fig = px.line(
    df,
    x="Date",
    y="Close",
    title=f"{stock} Closing Price"
)

st.plotly_chart(fig, width="stretch")

# Trading Volume
st.header("📊 Trading Volume")

fig2 = px.bar(
    df,
    x="Date",
    y="Volume",
    title="Daily Trading Volume"
)

st.plotly_chart(fig2, width="stretch")


st.header("📋 Stock Data")

st.dataframe(df)

# -------------------------
# AI INSIGHTS
# -------------------------

st.markdown("---")

st.header("🤖 AI Financial Report")

# Trend
first_price = float(df["Close"].iloc[0])
last_price = float(df["Close"].iloc[-1])
difference = last_price - first_price

if difference > 2:
    trend = "📈 Uptrend"
elif difference < -2:
    trend = "📉 Downtrend"
else:
    trend = "➖ Sideways"

# Recommendation
if current > average:
    recommendation = "BUY"
elif current < average:
    recommendation = "SELL"
else:
    recommendation = "HOLD"

# Risk
price_difference = highest - lowest

if price_difference < 20:
    risk = "🟢 Low Risk"

elif price_difference <= 50:
    risk = "🟡 Medium Risk"

else:
    risk = "🔴 High Risk"

# Display Cards

c1, c2, c3 = st.columns(3)

c1.metric("Trend", trend)

c2.metric("Recommendation", recommendation)

c3.metric("Risk", risk)

st.markdown("---")

st.subheader("📄 AI Summary")

# -------------------------
# AI Summary
# -------------------------

st.subheader("📄 AI Summary")

summary = f"""
### {stock} Stock Analysis

{stock} stock traded between **${lowest:.2f}**
and **${highest:.2f}** during the selected period.

📊 **Average Closing Price:** **${average:.2f}**

📈 **Current Market Trend:** **{trend}**

💡 **Recommendation:** **{recommendation}**

⚠️ **Risk Level:** **{risk}**
"""

st.markdown(summary)