import ccxt
import config

print(ccxt.exchanges)

for exchange in ccxt.exchanges:
    print (exchange)

exchange = ccxt.bybit({
    'apiKey': config.BYBIT_API_KEY,
    'secret': config.BYBIT_SECRET_KEY,
})


balance = exchange.fetch_balance()
print (balance)

markets = exchange.load_markets()
for market in markets:
    print (market)

ticker = exchange.fetch_ticker("BTC/USDT")
print (ticker)

a = exchange.fetch_ohlcv("BTC/USDT", timeframe="15m" ,limit=5)
for candle in a:
    print (candle)
