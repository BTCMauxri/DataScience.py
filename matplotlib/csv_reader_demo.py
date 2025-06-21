import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('investor_data.csv')     # CSV reader method from pandas
investor_ids = data['Investor_id']
investments = data['Ticker_Symbol']

ticker_counter = Counter() 

for each in investments:
    ticker_counter.update(each.split(';'))

tickers = []    # Will store the tickers
buyers = []     # Will store the buyers

for ticker, count in ticker_counter.items():
    tickers.append(ticker)
    buyers.append(count)

# Horizontal bar chart (y = tickers, x = buyers )
plt.barh(tickers, buyers)   

plt.title('Trending Tickers')
plt.xlabel('Buyers')
plt.ylabel('Tickers')

plt.tight_layout()
plt.show()





