from binance.client import Client
import os

client = Client(
    api_key=os.getenv("BINANCE_API_KEY", ""),
    api_secret=os.getenv("BINANCE_API_SECRET", "")
)

SYMBOL = "BTCUSDT"

def get_live_price(as_state=False):
    kline = client.get_klines(
        symbol=SYMBOL,
        interval=Client.KLINE_INTERVAL_1MINUTE,
        limit=1
    )[0]

    state = {
        "open": float(kline[1]),
        "high": float(kline[2]),
        "low": float(kline[3]),
        "close": float(kline[4]),
        "volume": float(kline[5]),
        "market_cap": 0
    }

    if as_state:
        return state

    return state["close"]
