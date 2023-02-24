                                                               SETUP

Following steps must be completed to get the BOT running:

1.Requesting API key and secret from your crypto exchange. 

2.Set your api key in the coresponding section of exchange as:
      apikey = your-exchange-api-key
      secret = your-binance-testnet-api-secret
      
3.Run pip install -r requirements.txt from the project root to install the required packages

4.Adjust other variables in the coresponding section of exchange according to your needs such as:
    exchange_id , defaultType , environment , interval , period , atr_multiplier and symbol.

5.Run python bot.py to start the BOT.

                                                             DESCRIPTION

supertrend bot using python, pandas, and ccxt

Working of the bot:
                   The buy and sell signals are generated when the indicator starts plotting either on top of the closing price or below the closing price.
A buy signal is generated when the ‘Supertrend’ closes below the price, and a sell signal is generated when it closes above the closing price.

The ATR formula is: 

                   “[(Prior ATR x(n-1)) + Current TR]/n” 
                   
                   where TR = max [(high − low), abs(high − previous close), abs(low – previous close)].

The supertrend indicator calculation is:

                                        Up = (high + low / 2 + multiplier  x  ATR
                                        
                                        Down = (high + low) / 2 – multiplier x ATR
