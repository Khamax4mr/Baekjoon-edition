from sys import stdin


def get_primes(n):
  is_prime = [False, False] + [True] * (n-1)
  for i in range(2, int(n**0.5)+1):
    if not is_prime[i]: continue

    for j in range(i*i, n+1, i):
      is_prime[j] = False

  return is_prime


n = int(stdin.readline())
assert 0 < n <= 100

nums = set(map(int, stdin.readline().split()))
assert all(0 < num <= 1000 for num in nums)

max_num = max(nums)
target_primes = get_primes(max_num)
primes = [i for i in nums if target_primes[i]]
print(len(primes))