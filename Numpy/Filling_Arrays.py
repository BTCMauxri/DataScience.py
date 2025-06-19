import numpy as np

a = np.full((2, 3, 4), 9)   # 2 arrays with 3 rows and 4 columns filled with 9's
print(a)                    # displays a

x_values = np.arange(0, 1010, 10) # array from 0 - 1000 in steps of 10
print(x_values)

x_values = np.linspace(0, 1000, 5) # array from 0 - 1000 and values wanted
print(x_values)
