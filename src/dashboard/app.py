import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf

st.markdown("----")

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
