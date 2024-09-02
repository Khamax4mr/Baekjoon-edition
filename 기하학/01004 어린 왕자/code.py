from sys import stdin

def is_cross(x1, y1, x2, y2, cx, cy, r):
  return is_in(x1, y1, cx, cy, r) != is_in(x2, y2, cx, cy, r)

def is_in(x1, y1, x2, y2, r):
  len = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
  return len < r

t = int(stdin.readline())
assert t >= 0

for _ in range(t):
  x1, y1, x2, y2 = map(int, stdin.readline().split())
  assert -1000 <= x1 <= 1000
  assert -1000 <= y1 <= 1000
  assert -1000 <= x2 <= 1000
  assert -1000 <= y2 <= 1000

  n = int(stdin.readline())
  assert 1 <= n <= 50

  cross_cnt = 0
  for _ in range(n):
    cx, cy, r = map(int, stdin.readline().split())
    assert -1000 <= cx <= 1000
    assert -1000 <= cy <= 1000
    assert 1 <= r <= 1000
    cross_cnt += is_cross(x1, y1, x2, y2, cx, cy, r)
  
  print(cross_cnt)