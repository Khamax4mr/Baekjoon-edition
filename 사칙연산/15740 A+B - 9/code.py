from sys import stdin

a, b = map(int, stdin.readline().split())
assert -pow(10, 10000) <= a <= pow(10, 10000)
assert -pow(10, 10000) <= b <= pow(10, 10000)
print(a + b)