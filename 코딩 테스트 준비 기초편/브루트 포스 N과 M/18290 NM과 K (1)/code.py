from sys import stdin

n, m, k = map(int, stdin.readline().split())
assert 1 <= n <= 10
assert 1 <= m <= 10
assert 1 <= k <= min(4, n*m)

board = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_expected = max(max(line) for line in board)
max_total = -10**6


def dfs(x, y, total, step):
  global max_total

  if step >= k:
    max_total = max(max_total, total)
    return

  expected = total + max_expected * (k-step)
  if expected < max_total: return
  
  for i in range(x, m):
    for j in range(y if i==x else 0, n):
      if visited[j][i]: continue

      nearby_skipped = False
      for dx, dy in directions:
        nx = i + dx
        ny = j + dy
        if nx < 0 or nx >= m: continue
        if ny < 0 or ny >= n: continue
        if not visited[ny][nx]: continue
        nearby_skipped = True
        break

      if nearby_skipped: continue
      
      visited[j][i] = True
      dfs(i, j, total + board[j][i], step+1)
      visited[j][i] = False 


dfs(0, 0, 0, 0)
print(max_total)