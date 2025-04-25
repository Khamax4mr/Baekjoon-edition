from sys import stdin


n = int(stdin.readline())
assert 0 <= n <= 50

nums = set(map(int, stdin.readline().split()))
assert all(2 <= num <= 1000000 for num in nums)

print(min(nums) * max(nums))