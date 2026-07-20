import yfinance as yf

print("Downloading Apple stock data...")

stock = yf.download("AAPL", period="1mo")

print(stock)

stock.to_csv("data/apple_stock.csv")

print("Data saved successfully!")