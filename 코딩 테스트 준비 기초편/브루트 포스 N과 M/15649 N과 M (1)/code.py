from sys import stdin
from itertools import permutations

n, m = map(int, stdin.readline().split())
assert 1 <= m <= n <= 8

print("\n".join(map(" ".join, permutations(map(str, range(1, n+1)), m))))