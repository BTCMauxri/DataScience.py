# collection = single  'variable' used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. Faster

# List of stock tickers
tickers = ['SPY', 'TSLA', 'NVDA', 'PLTR']

# prints each ticker in the list
print(f'Stock tickers in the list: ')
for each in tickers:
    print(f'{each}')

# prints the length of the list
print(f'The length of the list: {len(tickers)}')

# to check if a ticker is in the list:
in_list = input('Enter a ticker to check if it is in the list: ').strip().upper()

while in_list == '':
    in_list = input('Enter a ticker to check if it is in the list: ').strip().upper()

check = in_list in tickers  # This will equal a boolean

if check == True:
    print(f'The ticker ${in_list} is in the list')
else:
    print(f'The ticker {in_list} is not in the list')

# Add a ticker to the list and re print the length
tickers.append('CIBR')
print(f"Added '$CIBR' to the list: {tickers[:]}")
print(f'The new length of the list is: {len(tickers)}')

# tickers.remove('SPY') Will remove from the list
# tickers.insert(0, 'MSTR') Will add to list at index 0
# tickers.sort() Will sort list in alphabetical order
# tickers.reverse() Will reverse indexs
# tickers.clear() will clear a list
# tickers.index('SPY') Will return index if in list
# tickers.count('SPY') Will return how many of these in list

