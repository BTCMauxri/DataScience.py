# Import necessary libraries and tools
import numpy as np

# Create Matrix/ array A
A = np.array([[0, 1, 0], [0, 0, 1], [-1, 1, 0]])

# Now compute Eigen Values and Vectors
eValues, eVectors = np.linalg.eig(A)

# Finally print results
print(f"Eigenvalues: \n{eValues}\n")
print(f"Eigenvectors:\n {eVectors}\n")

# Specific Solution
# couldnt figure this out sadly:(
