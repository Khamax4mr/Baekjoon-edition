from sys import stdin


n = int(stdin.readline())
assert 1 <= n <= 1000000

print(sum([i * (n // i) for i in range(1, n + 1)]))