from sys import stdin
from itertools import combinations

n = int(stdin.readline())
assert 4 <= n <= 20 and n % 2 == 0

s = [list(map(int, stdin.readline().split())) for _ in range(n)]
assert all(s[i][i] == 0 for i in range(n))
assert all(1 <= s[i][j] <= 100 for i in range(n) for j in range(n) if i != j)

transport_s = list(zip(*s))
expected = sorted(sum(s[i]) + sum(transport_s[i]) for i in range(n))
total = sum(expected) // 2

min_level = min(abs(total - sum(lvs)) for lvs in combinations(expected, n//2))
print(min_level)