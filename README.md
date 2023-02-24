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