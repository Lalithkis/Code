import numpy as np
def perform_operations(n, m, array1, array2):
    A = np.array(array1)
    B = np.array(array2)
    addition = A + B
    subtraction = A - B
    multiplication = A * B
    integer_division = A // B
    modulo = A % B
    power = A ** B
    print(addition)
    print(subtraction)
    print(multiplication)
    print(integer_division)
    print(modulo)
    print(power)
n, m = map(int, input().split())
array1 = []
for _ in range(n):
    array1.append(list(map(int, input().split())))
array2 = []
for _ in range(n):
    array2.append(list(map(int, input().split())))
perform_operations(n, m, array1, array2)
