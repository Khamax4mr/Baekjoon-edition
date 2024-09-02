from sys import stdin

while True:
  a, b = map(int, stdin.readline().split())
  if a == 0 and b == 0: break
  assert 0 < a < 10
  assert 0 < b < 10
  print(a + b)