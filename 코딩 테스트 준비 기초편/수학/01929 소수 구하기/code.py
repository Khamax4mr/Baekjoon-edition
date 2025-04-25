from sys import stdin


def get_primes(n):
  is_prime = [False, False] + [True] * (n-1)
  for i in range(2, int(n**0.5)+1):
    if not is_prime[i]: continue

    for j in range(i*i, n+1, i):
      is_prime[j] = False

  return is_prime


min_n, max_n = map(int, stdin.readline().split())
assert 1 <= min_n <= 1000000
assert 1 <= max_n <= 1000000

target_primes = get_primes(max_n)[min_n : max_n+1]
primes = [str(min_n + id) for id, val in enumerate(target_primes) if val]
print("\n".join(primes))