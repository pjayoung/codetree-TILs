n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

max_safe_count = 0
best_k = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def can_go(x, y):
    if 0 <= x < n and 0 <= y < m:
        if not visited[x][y]:
            return True
    return False

def dfs(x, y, k):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny) and graph[nx][ny] > k:
            dfs(nx, ny, k)

for k in range(1, 101):
    visited = [[False] * m for _ in range(n)]
    safe_count = 0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] > k:
                dfs(i, j, k)
                safe_count += 1

    if safe_count > max_safe_count:
        max_safe_count = safe_count
        best_k = k

if max_safe_count == 0:
    best_k = 1

print(best_k, max_safe_count)