from sys import stdin

n, m = map(int, stdin.readline().split())
assert 4 <= n <= 500
assert 4 <= m <= 500

board = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_expected = max(max(line) for line in board)
max_total = 0


def dfs(x, y, total, step):
  global max_total

  if step >= 3:
    max_total = max(max_total, total)
    return
  
  expected = total + (3-step) * max_expected
  if expected < max_total: return

  for dx, dy in directions:
    nx = x + dx
    ny = y + dy
    if not 0 <= nx < m: continue
    if not 0 <= ny < n: continue
    if visited[ny][nx]: continue

    visited[ny][nx] = True
    if step == 1:
      dfs(x, y, total + board[ny][nx], step+1)

    dfs(nx, ny, total + board[ny][nx], step+1)
    visited[ny][nx] = False

  return max_total
 

for y in range(n):
  for x in range(m):
    visited[y][x] = True
    dfs(x, y, board[y][x], 0)
    visited[y][x] = False

print(max_total)