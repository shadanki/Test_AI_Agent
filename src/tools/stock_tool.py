import requests

def fetch_stock_price(symbol: str) -> float:
  # 例：Yahoo Finance API等を利用
  url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
  data = requests.get(url).json()
  return data9['quoteResponse']['result'][0]['regularmarketPrice']