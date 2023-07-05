import numpy as np

matrix = np.array([[3, 6, -2],
                   [0, 1, 0],
                   [0, 0, 1]])

eigenvalues, _ = np.linalg.eig(matrix)

print("Matrisin özdeğerleri:")
for eigenvalue in eigenvalues:
    print(eigenvalue)