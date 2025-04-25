from sys import stdin


def get_x_combo(board, n, y):
  max_combo, combo = 1, 1
  for i in range(1, n):
    combo = combo + 1 if board[y][i] == board[y][i - 1] else 1
    max_combo = max(max_combo, combo)
  return max_combo


def get_y_combo(board, n, x):
  max_combo, combo = 1, 1
  for i in range(1, n):
    combo = combo + 1 if board[i][x] == board[i - 1][x] else 1
    max_combo = max(max_combo, combo)
  return max_combo


n = int(stdin.readline())
assert 3 <= n <= 50

candy_type = {'C', 'P', 'Z', 'Y'}
candies = [list(stdin.readline().strip()) for _ in range(n)]
assert all(candy in candy_type for line in candies for candy in line)

combo = 0
for x in range(n):
  combo = max(combo, get_x_combo(candies, n, x), get_y_combo(candies, n, x))

  for y in range(n):
    if y + 1 < n:
      candies[y][x], candies[y+1][x] = candies[y+1][x], candies[y][x]
      combo = max(combo, get_y_combo(candies, n, x), get_x_combo(candies, n, y), get_x_combo(candies, n, y + 1))
      candies[y][x], candies[y+1][x] = candies[y+1][x], candies[y][x]
    
    if x + 1 < n:
      candies[y][x], candies[y][x+1] = candies[y][x+1], candies[y][x]
      combo = max(combo, get_x_combo(candies, n, y), get_y_combo(candies, n, x), get_y_combo(candies, n, x + 1))
      candies[y][x], candies[y][x+1] = candies[y][x+1], candies[y][x]

print(combo)