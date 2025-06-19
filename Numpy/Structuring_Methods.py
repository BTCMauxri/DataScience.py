import numpy as np

a = np.array([[1, 2, 3, 4, 5],      # a 4 * 5 array
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]])

print(f"The dimensions of array a is: {a.shape}")
print(f"Now re-shaping the array into a compatible dimension: \n{a.reshape(2, 10)}")
# reshape only temporarily changes the array use a.resize(2, 10) to update fully
print(a.flatten())  # flattens the array to one row
print(f"\nNow swapping the axis of the array: \n{a.transpose()}")

a1 = np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10]])

a2 = np.array([[11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20]])

z = np.concatenate((a1, a2), axis = 0)  #0 = rows, 1 = columns
print(f"\n{z}")

x = np.stack((a1, a2))  # stacks both arrays into one array, adds another dimension
print(f"\n{x}")
# there is also .split(), .min(), .max(), .mean(), .std(), .sum() etc