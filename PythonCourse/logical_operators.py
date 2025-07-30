# Logical Operators = (or, and , not) used to evaluate conditions

# In this example I demonstate a simple scenario 

greed_high = True
SPY = 638

if SPY > 600 and greed_high:
    print(f'Not a good time to buy')

elif SPY < 600 and not(greed_high):
    print(f'Consider buying')

else:
    print(f'Sit on your hands for now')