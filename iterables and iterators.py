from math import factorial
def comb(n, k):
    if k > n or k < 0:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))
def calculate_probability(n, letters, k):
    target_letter = letters[0]
    target_indices = [i for i, letter in enumerate(letters) if letter == target_letter]
    target_count = len(target_indices)
    total_tuples = comb(n, k)
    non_target_indices = n - target_count
    non_target_tuples = comb(non_target_indices, k) if k <= non_target_indices else 0
    favorable_tuples = total_tuples - non_target_tuples
    probability = favorable_tuples / total_tuples
    return round(probability, 4)
if __name__ == '__main__':
    n = int(input().strip())
    letters = input().strip().split()
    k = int(input().strip())
    result = calculate_probability(n, letters, k)
    print(f"{result:.4f}")
