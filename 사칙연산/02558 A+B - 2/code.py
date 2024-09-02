from sys import stdin

a, b = map(int, stdin.readlines())
assert 0 < a < 10
assert 0 < b < 10
print(a + b)