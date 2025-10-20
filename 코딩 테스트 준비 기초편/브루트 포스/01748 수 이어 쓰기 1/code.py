from sys import stdin

n = int(stdin.readline())
assert 1 <= n <= 100000000

n_len = len(str(n))
completed_len = sum((10**i - 10**(i-1))*i for i in range(1, n_len))
print(completed_len + (n - 10**(n_len-1) + 1) * n_len)