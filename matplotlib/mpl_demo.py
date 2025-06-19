# Mauricio Villegas | matplotlib demo/practice
# Tracking the price of three stock tickers over a span of 10 years
# Tickers --> $TSLA, $AMZN, $NVDA (my favorite stocks)
# link to plot format settings: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# import matplot and rename for simplicity
from matplotlib import pyplot as plt
plt.style.use('Solarize_Light2')

# years will be the x-axis of our plot
years = [2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020]

# 1st I grab the prices of $SPY in order of years at the month of january for each year
AMZN = [6.81, 9.07, 8.79, 12.80, 19.94, 15.63, 
        32.81, 37.90, 58.60, 73.26, 90.22]

# Plot and customize $AMZN line
plt.plot(years, AMZN, color = '#FFA500', label = '$AMZN')   

# 2nd I do the same for $TSLA
TSLA = [1.20, 1.79, 1.93, 2.33, 9.99, 14.86, 15.38,
        14.32, 20.80, 20.41, 28.30]

plt.plot(years, TSLA, color = '#FF0000', label = '$TSLA')

# Now I do the same for $NVDA
NVDA = [.46, .39, .36, .31, .40, .50, .81, 2.61,
        4.89, 3.27, 5.41]

plt.plot(years, NVDA, color = '#008000', label = '$NVDA')


plt.xlabel('Decade Price Action')                   # x-label
plt.ylabel('Share Price at Start of Year')          # y-label
plt.legend()                                        # Shows the labels for tickers
plt.grid(True)
plt.tight_layout()
plt.show()                                          # Displays the plot