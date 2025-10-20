from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
assert 1 <= m <= n <= 8

nums = sorted(map(int, stdin.readline().split()))
assert all(0 < num <= 10000 for num in nums)

print("\n".join(map(" ".join, combinations(map(str, nums), m))))