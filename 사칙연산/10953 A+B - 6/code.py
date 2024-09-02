from sys import stdin

t = int(stdin.readline())
assert t >= 0

for _ in range(t):
  a, b = map(int, stdin.readline().split(','))
  assert 0 < a < 10
  assert 0 < b < 10
  print(a + b)