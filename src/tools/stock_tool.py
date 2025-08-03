# src/tools/stock_tool.py
import yfinance as yf

def fetch_stock_price(symbol: str) -> float:
    """
    yfinance を使って直近の終値を取得します。
    symbol: "MSFT" のように山かっこなしで渡してください。
    """
    # 余分な <> があれば除去
    symbol = symbol.strip().strip("<>")
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    if data.empty:
        raise ValueError(f"No data found for symbol: {symbol}")
    # 終値 (Close) の最新行を返す
    return float(data["Close"][-1])
