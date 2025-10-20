from sys import stdin

t = int(stdin.readline())
assert t >= 0

nums = list(map(int, stdin.readlines()))
assert all(0 < n < 11 for n in nums)

dp = [0, 1, 2, 4]
for i in range(4, max(nums)+1):
  dp.append(sum(dp[i-3:i]))

for n in nums:
  print(dp[n])