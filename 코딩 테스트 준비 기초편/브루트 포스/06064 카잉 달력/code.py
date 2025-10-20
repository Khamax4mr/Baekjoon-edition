from sys import stdin
from math import gcd, lcm


t = int(stdin.readline())
assert t >= 0

for _ in range(t):
  m, n, x, y = map(int, stdin.readline().split())
  assert 1 <= m <= 40000
  assert 1 <= n <= 40000
  assert 1 <= x <= m
  assert 1 <= y <= n

  if (y - x) % gcd(m, n) != 0:
    print(-1)
  else:
    for i in range(x, lcm(m, n)+1, m):
      if (i - y) % n > 0: continue
      print(i)
      break