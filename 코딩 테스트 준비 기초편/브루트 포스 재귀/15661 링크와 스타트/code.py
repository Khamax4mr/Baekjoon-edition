from sys import stdin

n = int(stdin.readline())
assert 4 <= n <= 20

s = [list(map(int, stdin.readline().split())) for _ in range(n)]
assert all(s[i][i] == 0 for i in range(n))
assert all(1 <= s[i][j] <= 100 for i in range(n) for j in range(n) if i != j)

transport_s = list(zip(*s))
expected = sorted(sum(s[i]) + sum(transport_s[i]) for i in range(n))
total = sum(expected) // 2

cand_levels = {0}
for i in expected:
  cand_levels |= {i+j for j in cand_levels}

min_level = min(abs(total - lv) for lv in cand_levels)
print(min_level)