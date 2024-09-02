from sys import stdin

def get_zero_one_count(n):
  zero_cnt, one_cnt = 1, 0
  for _ in range(n):
    zero_cnt, one_cnt = one_cnt, one_cnt + zero_cnt
  return zero_cnt, one_cnt


t = int(stdin.readline())
assert t >= 0

for _ in range(t):
  n = int(stdin.readline())
  assert 0 <= n <= 40

  zero_cnt, one_cnt = get_zero_one_count(n)
  print(zero_cnt, one_cnt)