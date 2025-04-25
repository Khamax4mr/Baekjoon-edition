from sys import stdin
from itertools import product


def get_candidates(n, valids):
  candidates = [] 
  distance = abs(n - 100)
  upper_bound = min(999900, n + distance)
  lower_bound = max(0, n - distance)

  for l in range(1, len(str(upper_bound)) + 1):
    for p in product(valids, repeat=l):
      if l > 1 and p[0] == 0: continue
      num = int(''.join(map(str, p)))

      if not lower_bound <= num <= upper_bound: continue
      candidates.append(num)
  
  candidates.append(n)
  candidates.sort()
  return candidates


def get_closest_candidates(n, invalids):
  valids = [i for i in range(0, 10) if i not in invalids]
  candidates = get_candidates(n, valids)

  id = candidates.index(n)
  high_candidate = candidates[id + 1] if id + 1 < len(candidates) else 1000000
  low_candidate = candidates[id - 1] if id - 1 >= 0 else 1000000
  return high_candidate, low_candidate


n = int(stdin.readline())
m = int(stdin.readline())
assert 0 <= n <= 500000
assert 0 <= m <= 10

broken_btns = set(map(int, stdin.readline().split()))
assert all(0 <= btn < 10 for btn in broken_btns)

brokens = len(broken_btns)
distance = abs(n - 100)

if brokens == 0:
  print(min(len(str(n)), distance))
elif brokens == 10:
  print(distance)
else:
  target_btns = set(int(i) for i in str(n))
  if not target_btns & broken_btns:
    print(min(len(str(n)), distance))
  else:
    high_cand, low_cand = get_closest_candidates(n, broken_btns)
    high_moves = len(str(high_cand)) + abs(high_cand - n)
    low_moves = len(str(low_cand)) + abs(low_cand - n)
    print(min(distance, high_moves, low_moves))