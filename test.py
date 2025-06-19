import numpy as np

A = np.array([[0, 1, 0], [0, 0, 1], [-1, 1, 0]])

At = np.transpose(A)

AtA = np.dot(At, A)

det = np.linalg.det(AtA)

#print(AtA)
#inverse = np.linalg.inv(AtA)

print(det)

