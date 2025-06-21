# Mauricio Villegas | matplotlib demo/practice
# This python script demonstrates the use of the csv tool for reading data from a csv file
# Here I am plotting the buyers on three tickers ($TSLA, $AMZN, $NVDA)
# I use a horizontal bar chart to display this data
import csv                              # csv library
import numpy as np                      
from collections import Counter         # counter will count each ticker
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# Open csv file in directory
with open('investor_data.csv') as csv_file: 
    # reads the csv and creates a Dict out of the data
    csv_reader = csv.DictReader(csv_file)   

    # Variable will be a counter object
    ticker_counter = Counter()

    # Count and update the counts for each ticker in the csv_reader Dict
    for each_row in csv_reader:
        ticker_counter.update(each_row['Ticker_Symbol'].split(';'))

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


