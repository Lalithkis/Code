import numpy as np
def calculate_determinant():
    n = int(input().strip())
    matrix = []
    for _ in range(n):
        row = list(map(float, input().strip().split()))
        matrix.append(row)
    matrix = np.array(matrix)
    determinant = np.linalg.det(matrix)
    determinant = round(determinant, 2)
    print(determinant)
calculate_determinant()
