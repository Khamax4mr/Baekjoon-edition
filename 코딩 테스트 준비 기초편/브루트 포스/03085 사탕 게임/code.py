from sys import stdin


def is_linked(board, n, i, j):
  return j+1 < n and board[i][j] == board[i][j+1]


def is_next_swap_linked(board, n, i, j):
  return j+2 < n and board[i][j] == board[i][j+2]


def is_upper_swap_linked(board, n, i, j):
  is_prev_linked = i-1 >= 0 and j-1 >= 0 and board[i-1][j] == board[i][j-1]
  is_next_linked = i-1 >= 0 and j+1 < n and board[i-1][j] == board[i][j+1]
  return is_prev_linked or is_next_linked


def is_lower_swap_linked(board, n, i, j):
  is_prev_linked = i+1 < n and j-1 >= 0 and board[i+1][j] == board[i][j-1]
  is_next_linked = i+1 < n and j+1 < n and board[i+1][j] == board[i][j+1]
  return is_prev_linked or is_next_linked


def get_max_combo(board, n):
    high_combo = []

    for i in range(n):
      combo_id = 0

      for j in range(n):
        if is_linked(board, n, i, j): continue
        high_combo.append(j - combo_id + 1)

        if is_next_swap_linked(board, n, i, j):
          high_combo[-1] += 1

        if is_upper_swap_linked(board, n, i, j):
          combo = 1
          for k in range(j-1, -1, -1):
            if board[i][k] != board[i-1][j]: break
            combo += 1
          for k in range(j+1, n):
            if board[i][k] != board[i-1][j]: break
            combo += 1
          high_combo.append(combo)

        if is_lower_swap_linked(board, n, i, j):
          combo = 1
          for k in range(j-1, -1, -1):
            if board[i][k] != board[i+1][j]: break
            combo += 1
          for k in range(j+1, n):
            if board[i][k] != board[i+1][j]: break
            combo += 1
          high_combo.append(combo)

        combo_id = j + 1

    return max(high_combo)


n = int(stdin.readline())
assert 3 <= n <= 50

candy_type = {'C', 'P', 'Z', 'Y'}
candies = [list(stdin.readline().strip()) for _ in range(n)]
assert all(candy in candy_type for line in candies for candy in line)

transport_candies = list(zip(*candies))
print(max(get_max_combo(candies, n), get_max_combo(transport_candies, n)))