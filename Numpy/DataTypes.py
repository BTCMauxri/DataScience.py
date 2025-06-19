import numpy as np

a = np.array([[1, 2, 3],
              [4, "Hello", 6],
              [7, 8, 9]])

print(a.dtype)      # The array is of type string
print(type(a[0,0])) # This index value is 1 but shows that it is a string
