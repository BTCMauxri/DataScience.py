# input() = A function that prompts the user to enter data
# returns the entered data as a String

price = input("What is the stock price of $TSLA?: ")

print(f"The stock price of Tesla stock is: ${price} per share.")

shares = input("How many shares of Tesla do you own?: ")

price = float(price)
shares = float(shares)

value = (price * shares)

print(f"You have ${value} worth of Tesla stock in your portfolio.")

