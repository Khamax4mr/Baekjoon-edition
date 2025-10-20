from sys import stdin


def get_primes(n):
  is_prime = [False, False] + [True] * (n-1)
  for i in range(2, int(n**0.5)+1):
    if not is_prime[i]: continue
    for j in range(i*i, n+1, i):
      is_prime[j] = False
  return is_prime


def goldbach(is_prime, n):
  for i in range(3, n//2 + 1, 2):
    if not is_prime[i]: continue
    if not is_prime[n-i]: continue
    return i, n-i
  return 0, 0


nums = list(map(int, stdin.readlines()))
nums.remove(0)
assert all(6 <= n <= 1000000 for n in nums)

is_prime = get_primes(max(nums))
for n in nums:
  a, b = goldbach(is_prime, n)
  if a == 0 and b == 0:
    print("Goldbach's conjecture is wrong.")
  else:
    print(n, "=", a, "+", b)