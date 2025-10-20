from sys import stdin

n = int(stdin.readline())
assert 1 <= n <= 15

schedules = [list(map(int, stdin.readline().split())) for _ in range(n)]
t = [int(row[0]) for row in schedules]
p = [int(row[1]) for row in schedules]
assert all(1 <= time <= 5 for time in t)
assert all(1 <= pay <= 1000 for pay in p)

dp = [0 for _ in range(n+1)]
for i in range(n):
  for j in range(i+t[i], n+1):
    if dp[j] >= dp[i] + p[i]: continue
    dp[j] = dp[i] + p[i]

print(dp[-1])