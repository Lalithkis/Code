def check_polynomial_evaluation(x, k, polynomial):
    variables = {'x': x}
    result = eval(polynomial, {}, variables)
    return result == k
x, k = map(int, input().split())
polynomial = input()
print(check_polynomial_evaluation(x, k, polynomial))
