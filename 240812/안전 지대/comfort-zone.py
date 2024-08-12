n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

max_safe_count = 0
best_k = 0

min_height = min(min(row) for row in graph)
max_height = max(max(row) for row in graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def can_go(x, y):
    if 0 <= x < n and 0 <= y < m and not visited[x][y]:
        return True
    return False

def dfs(x, y, k):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny) and graph[nx][ny] > k:
            dfs(nx, ny, k)

for k in range(min_height, max_height+1):
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

# 안전 구역이 발견되지 않으면 최소 k는 1로 설정
if max_safe_count == 0:
    best_k = 1

print(best_k, max_safe_count)