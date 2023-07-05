import numpy as np

def linear_dependency(vectors):
    matrix = np.array(vectors)
    rank = np.linalg.matrix_rank(matrix)
    num_vectors = len(vectors)

    if rank < num_vectors:
        print("Vektörler lineer bağımlıdır.")
    else:
        print("Vektörler lineer bağımsızdır.")

# Örnek vektörler

a=-1
b=0

vectors = [[1, 2, 1, 3],
           [1, -1, 2, 0],
           [1, a, 2, b]]

linear_dependency(vectors)
