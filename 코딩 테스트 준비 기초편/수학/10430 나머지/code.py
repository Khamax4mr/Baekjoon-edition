from sys import stdin

a, b, c = map(int, stdin.readline().split())
assert 2 <= a <= 10000
assert 2 <= b <= 10000
assert 2 <= c <= 10000

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)