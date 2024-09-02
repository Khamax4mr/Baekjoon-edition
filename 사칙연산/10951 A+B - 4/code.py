from sys import stdin

for line in stdin:
  a, b = map(int, line.split())
  assert 0 < a < 10
  assert 0 < b < 10
  print(a + b)