from sys import stdin
from math import lcm

e, s, m = map(int, stdin.readline().split())
assert 1 <= e <= 15
assert 1 <= s <= 28
assert 1 <= m <= 19

for i in range(lcm(15, 28, 19) + 1):
  if i % 15 + 1 != e: continue
  if i % 28 + 1 != s: continue
  if i % 19 + 1 != m: continue
  print(i + 1)
  break