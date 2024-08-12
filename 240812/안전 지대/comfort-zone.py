import sys

sys.setrecursionlimit(2500)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, K, visited):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] > K:
            dfs(nx, ny, K, visited)

def count_safe_zones(K):
    visited = [[False] * m for _ in range(n)]
    safe_zone_count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] > K and not visited[i][j]:
                dfs(i, j, K, visited)
                safe_zone_count += 1

    return safe_zone_count

def find_max_safe_zones():
    max_height = max(max(row) for row in graph)
    max_safe_zones = 0
    optimal_K = 0

    for K in range(1, max_height + 1):
        safe_zone_count = count_safe_zones(K)
        if safe_zone_count > max_safe_zones:
            max_safe_zones = safe_zone_count
            optimal_K = K

    return optimal_K, max_safe_zones

# 결과 출력
optimal_K, max_safe_zones = find_max_safe_zones()
print(optimal_K, max_safe_zones)