# basic examples of some math functions
import math

TSLA = 301.99
NVDA = 160.0
SPY = 625

x1 = round(TSLA)    # rounds the values of TSLA
x2 = abs(NVDA)      # returns absolute value of NVDA
x3 = pow(4, 3)      # 4 cubed
x4 = min(TSLA, NVDA, SPY)   # returns smallest values
x5 = max(TSLA, NVDA, SPY)   # returbs largest value

# The following are only available by importing the math library
a1 = math.sqrt(SPY) # gets the square root of SPY
print(math.pi)      # returns pi
a2 = math.floor(TSLA)   # rounds down
a3 = math.ceil(TSLA)    # rounds up
