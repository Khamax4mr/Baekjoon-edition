from sys import stdin


def get_primes(n):
  is_prime = [False, False] + [True] * (n-1)
  for i in range(2, int(n**0.5)+1):
    if not is_prime[i]: continue

    for j in range(i*i, n+1, i):
      is_prime[j] = False

  return is_prime


def goldbach(is_prime, n):
  a, b = 0, 0
  for i in range(3, int(n/2)+1, 2):
    if is_prime[i] and is_prime[n-i]:
      a, b = i, n - i
      break
  return a, b


nums = list(map(int, stdin.readlines()))
assert 0 in nums
nums.remove(0)
assert all(6 <= n <= 1000000 for n in nums)

max_n = max(nums)
is_prime = get_primes(max_n)

for n in nums:
  a, b = goldbach(is_prime, n)
  if a == 0 and b == 0:
    print("Goldbach's conjecture is wrong.")
  else:
    print(n, "=", a, "+", b)