# numpy is imported and assigned to np
import numpy as np

# example of a normal array 
print(f"Example of a normal array and operations: ")
a = [1, 2, 3, 4, 5]
print(a)        # prints the whole array
print(a[1])     # prints position 2 of the array
print(a[1:4])   # prints from position 1:4 inclusive
print(a[-1])    # prints the last position
print(type(a))  # displays the type of array

# The same can be done in numpy arrays which are optimized for linear algebra
print(f"\nNow showing a numpy array: ")
b = np.array([1, 2, 3, 4, 5])
print(b)        #displays the numpy array
print(type(b))  # displays type of array --> ndarray
# Can still do the following operations
print(b)        # prints the whole array
print(b[1])     # prints position 2 of the array
print(b[1:4])   # prints from position 1:4 inclusive
print(b[-1])    # prints the last position
print(type(b))  # displays the type of array

# Now multi dimensional arrays
print(f"\nNow demonstrating a multi-dimensional array: ")
a_mul = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(a_mul[0])         # displays first row
print(a_mul[0, 1])      # displays 1st row 2nd index
print(f"\nNow showing some operations on the array:")
print(a_mul.shape)      # displays the dimensions of the array
print(a_mul.size)       # displays total elements in the array