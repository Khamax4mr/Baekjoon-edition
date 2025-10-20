from sys import stdin


heights = list(map(int, stdin.readlines()))
assert all(0 < height < 100 for height in heights)

remains = sum(heights) - 100
spy1, spy2 = 0, 0
for h1 in heights:
  h2 = remains - h1
  if h1 == h2: continue
  if h2 not in heights: continue
  spy1, spy2 = h1, h2
  break

heights.remove(spy1)
heights.remove(spy2)
heights.sort()
print("\n".join(str(n) for n in heights))