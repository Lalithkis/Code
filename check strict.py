A = set(map(int, input().split()))
n = int(input())
is_strict_superset = True
for _ in range(n):
    other_set = set(map(int, input().split()))
    if not (A > other_set):
        is_strict_superset = False
        break
print(is_strict_superset)
