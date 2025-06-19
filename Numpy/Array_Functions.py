import numpy as np

a = np.array([1, 2, 3])
a = np.append(a, [7, 8, 9]) # takes in the array and what values u are adding
print(a)                    # display the updated array
a = np.insert(a, 3, [4, 5, 6])
print(a)                    # insert(array to be inserted to, position, values)
print(np.delete(a, 1))             # this will delete what ever is at index 1
print(np.delete(a, 1, 0))          # This deletes the row at index 1
print(np.delete(a, 0, 1))          # This deletes column 0 
# column is 1 and row is 0 in the third parameter
