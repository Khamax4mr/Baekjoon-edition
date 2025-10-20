from sys import stdin

n = int(stdin.readline())
assert 0 <= n <= 50

nums = list(map(int, stdin.readline().split()))
for num in nums:
  assert 2 <= num <= 1000000
assert nums and set(nums)

print(min(nums) * max(nums))