from sys import stdin
from itertools import combinations

l, c = map(int, stdin.readline().split())
assert 3 <= l <= c <= 15

alphabets = sorted(stdin.readline().split())
vowels = ['a', 'e', 'i', 'o', 'u']

for pwd in combinations(alphabets, l):
  n_vowel = [v in pwd for v in vowels].count(True)
  if n_vowel < 1: continue
  if l - n_vowel < 2: continue
  print("".join(pwd))