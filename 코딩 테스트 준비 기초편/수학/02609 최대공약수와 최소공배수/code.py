from sys import stdin

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a


a, b = map(int, stdin.readline().split())
assert 0 < a <= 10000
assert 0 < b <= 10000

print(gcd(a, b))
print(a * b // gcd(a, b))