from sys import stdin
from itertools import product


def get_prefix(digits):
  prefix = []
  for a, b in product(digits, repeat=2):
    if a == 0: continue
    prefix.append(a*10 + b)
  return prefix


def get_high_number(target, valids):
  digits = valids
  prefix = digits + get_prefix(valids)

  def backtrack(buf, id, prefix_eq):
    result = None

    for d in digits if id > 0 else prefix:
      if id == 0 and d == 0: continue
      if prefix_eq and d < target[id]: continue

      next_prefix_eq = prefix_eq and d == target[id]
      buf.append(d)

      if id == len(target)-1:
        return int(''.join(map(str, buf)))

      result = backtrack(buf, id+1, next_prefix_eq)
      if result: break
      
      buf.pop()

    return result
  
  return backtrack([], 0, True)


def get_lower_number(target, valids):
  digits = valids[::-1] + [None]

  def backtrack(buf, start_id, id, prefix_eq):
    result = None
    
    for d in digits:
      if start_id == id and id+1 == len(target) and d is None: continue
      if start_id == id and id+1 < len(target) and d == 0: continue
      if start_id < id and d is None: continue
      if prefix_eq and d and d > target[id]: continue

      next_start_id = id+1 if d is None else start_id
      next_prefix_eq = prefix_eq and d == target[id]
      buf.append(d)

      if id == len(target)-1:
        return int(''.join(map(str, buf[start_id:])))

      result = backtrack(buf, next_start_id, id+1, next_prefix_eq)
      if result: break

      buf.pop()
    
    return result

  return backtrack([], 0, 0, True)


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
  target = list(map(int, str(n)))
  if not set(target) & broken_btns:
    print(min(len(str(n)), distance))
  else:
    valid_btns = [i for i in range(0, 10) if i not in broken_btns]
    high_n = get_high_number(target, valid_btns) 
    low_n = get_lower_number(target, valid_btns)
    high_moves = len(str(high_n)) + abs(high_n - n) if high_n is not None else 1000000
    low_moves = len(str(low_n)) + abs(low_n - n) if low_n is not None else 1000000
    print(min(distance, high_moves, low_moves))