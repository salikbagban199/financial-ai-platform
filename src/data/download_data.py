import yfinance as yf
import os

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Dictionary of stocks
stocks = {
    "apple": "AAPL",
    "tesla": "TSLA",
    "microsoft": "MSFT",
    "amazon": "AMZN",
    "google": "GOOGL"
}

# Download each stock
for name, ticker in stocks.items():
    print(f"Downloading {name.title()} ({ticker})...")

    df = yf.download(ticker, period="1mo")

    filename = f"data/{name}_stock.csv"

    df.to_csv(filename)

    print(f"✅ Saved: {filename}")

print("\nAll stock data downloaded successfully!")