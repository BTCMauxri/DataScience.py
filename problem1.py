# import the numpy library as np
import numpy as np

# Creating arrays from data set provided
X = np.array([[1, 2], [1, 3], [1, 4], [1, 5]])
y = np.array([81, 93, 91, 97])

# X transpose computation
XT = np.transpose(X)

# (X^T) * X Computation (X Transpose times X)
XTX = np.dot(XT, X)

# (X^T) * Y Computation (X Transpose times Y)
XTY = np.dot(XT, y)

# Compute the inverse of X Transpose tims X
inverse = np.linalg.inv(XTX)

# get coefficients with B formula
B = np.dot(inverse, XTY)

# Finally print results
print(B)



