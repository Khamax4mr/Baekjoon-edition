from sys import stdin

n = int(stdin.readline())
assert 1 <= n <= 1000000

f = [0 for _ in range(n + 1)]
print(sum([i * (n // i) for i in range(1, n + 1)]))