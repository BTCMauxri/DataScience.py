# Mauricio Villegas | matplotlib demo/practice
# This script will organize the current top 5 
# DeFi coins by market cap (not including $USDC)

from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('Solarize_Light2')

data = pd.read_csv('crypto_top5.csv') # CSV reader

# The following arrays will store respected data
Coins = []
Market_Cap = []

# Iterate through the data array to organize data into respected arrays
for index, row in data.iterrows():
    Coins.append(row['Coin'])
    Market_Cap.append(row['Market_Cap'])

# Explode will show what value to amplify ( I am amplifying Bitcoin since it dominates overall market caps)
explode = [0.1, 0, 0, 0, 0]
# Plot the pie chart
plt.pie(Market_Cap, labels = Coins, explode = explode, shadow = True,
        startangle = 90, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black'})

plt.title('Top 5 DeFI Dominating Coins by Market Cap')
plt.tight_layout()
plt.show()
