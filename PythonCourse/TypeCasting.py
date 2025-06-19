# Typecasting = the process of converting a variable from one data type
# to another -> str(), int(), float(), bool()

stock_ticker = "$TSLA"
year = 2025
stock_price = 365.92
beat_earnings = True

# to find the type of a variable do:
print(type(stock_price))    # float

#type cast the stock price into an int
print(int(stock_price))

# you can type cast an int <-> float
# int -> str
# str -> bool (if string is empty -> False)