from sys import stdin

while True:
  try:
    n  = int(stdin.readline())
    assert (n % 2) or (n % 5)
    assert 1 <= n <= 10000

    remain, cnt = 1 % n, 1
    while remain:
      remain = (10 * remain + 1) % n
      cnt += 1
    print(cnt)
  except: break