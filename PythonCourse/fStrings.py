# Variable = A container for a value (string, integer, float, boolean)
#            A Variale behaves as if it was the value it contains

#The following are variables, technically these are all strings
stock_ticker = '$TSLA'
price = '$339'
ceo = 'Elon Musk'

#The following are integers
stock_price = 339
quantity = 3220000000
market_cap = int(stock_price * quantity)

#Float
exact_price = 365.92

#Boolean
beat_earnings = True

print(f"The CEO of Tesla is " + ceo + ", the company ticker symbol is " + 
      stock_ticker + " and the price per share is " + price)

print(f"There are a total of {quantity} shares of Tesla stock, " +
    f"this means the total market cap of the company is ${market_cap} ")

print(f"The exact stock price is ${exact_price}")

print(f"Did Tesla beat earnings ?: {beat_earnings}")

# The following is a simple if else statement

if beat_earnings:
    print("Tesla indeed did beat earnings!")
else:
    print("Tesla did not beat earnings")