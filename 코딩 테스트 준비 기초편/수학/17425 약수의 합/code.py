from sys import stdin

f = [0] * (1000000 + 1)
g = [0] * (1000000 + 1)
for i in range(1, 1000000 + 1):
  for j in range(1, 1000000 // i + 1):
    f[i * j] += i
  g[i] = g[i-1] + f[i]

t = int(stdin.readline())
assert 1 <= t <= 100000

for i in range(t):
  n = int(stdin.readline())
  assert 1 <= n <= 1000000
  print(g[n])