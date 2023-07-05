def determinant_4x4(matrix):
    if len(matrix) != 4 or len(matrix[0]) != 4:
        raise ValueError("Matrisin boyutu 4x4 olmalıdır.")

    det = 0
    for i in range(4):
        sub_matrix = [[0] * 3 for _ in range(3)]
        for j in range(1, 4):
            for k in range(4):
                if k < i:
                    sub_matrix[j-1][k] = matrix[j][k]
                elif k > i:
                    sub_matrix[j-1][k-1] = matrix[j][k]

        sign = (-1) ** (i % 2)
        det += sign * matrix[0][i] * determinant_3x3(sub_matrix)

    return det


def determinant_3x3(matrix):
    if len(matrix) != 3 or len(matrix[0]) != 3:
        raise ValueError("Matrisin boyutu 3x3 olmalıdır.")

    det = 0
    for i in range(3):
        sub_matrix = [[0] * 2 for _ in range(2)]
        for j in range(1, 3):
            for k in range(3):
                if k < i:
                    sub_matrix[j-1][k] = matrix[j][k]
                elif k > i:
                    sub_matrix[j-1][k-1] = matrix[j][k]

        sign = (-1) ** (i % 2)
        det += sign * matrix[0][i] * determinant_2x2(sub_matrix)

    return det


def determinant_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("Matrisin boyutu 2x2 olmalıdır.")

    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


# Örnek kullanım
matrix = [[2, -1, 0, -2],
          [4, 1, 0, 3],
          [-1, -2, 3, 1],
          [0, -3, 0, 5]]

det = determinant_4x4(matrix)
print("Matrisin determinantı:", det)