from sys import stdin

a, b = map(int, stdin.readline().split())
assert 0 < a <= 10000
assert 0 < b <= 10000
result = str(a // b) + '.'

for i in range(1000):
  a = a % b * 10
  if a == 0: break
  result += str(a // b)
print(result)