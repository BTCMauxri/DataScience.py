# In this excercise I reverse a string in a simple manner

credit_number = '1234-5678-6578-8273'
print(f'Credit card number: {credit_number}')
print(f'Last 4 digits: {credit_number[-4:]}')

# [start, end, step]
credit_number = credit_number[::-1]  # set the step to -1

print(f'Credit number in reverse order: {credit_number}')