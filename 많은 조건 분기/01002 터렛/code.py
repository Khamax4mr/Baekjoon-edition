from sys import stdin

def get_intersection_count(x1, y1, r1, x2, y2, r2):
  if x1 == x2 and y1 == y2 and r1 == r2:
    return -1
  else:
    point_dist = get_distance(x1, y1, x2, y2)
    min_r, max_r = min(r1, r2), max(r1, r2)
    if point_dist == max_r + min_r or point_dist == max_r - min_r:
      return 1
    elif max_r - min_r < point_dist < max_r + min_r:
      return 2
  return 0

def get_distance(x1, y1, x2, y2):
  return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


t = int(stdin.readline())
assert t >= 0

for _ in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().split())
  assert -10000 <= x1 <= 10000
  assert -10000 <= y1 <= 10000
  assert 1 <= r1 <= 10000
  assert -10000 <= x2 <= 10000
  assert -10000 <= y2 <= 10000
  assert 1 <= r2 <= 10000
  print(get_intersection_count(x1, y1, r1, x2, y2, r2))