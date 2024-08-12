import sys
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def count_safe_zones(grid, N, M, K):
    visited = [[False] * M for _ in range(N)]
    
    def is_safe(x, y):
        return 0 <= x < N and 0 <= y < M and not visited[x][y] and grid[x][y] > K
    
    def dfs(x, y):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            # 상하좌우 탐색
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if is_safe(nx, ny):
                    stack.append((nx, ny))
    
    safe_zone_count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] > K and not visited[i][j]:
                # 새로운 안전 영역 발견
                dfs(i, j)
                safe_zone_count += 1
                
    return safe_zone_count

def find_max_safe_zones(N, M, heights):
    max_height = max(max(row) for row in heights)
    max_safe_zones = 0
    optimal_K = 0

    for K in range(1, max_height + 1):
        safe_zone_count = count_safe_zones(heights, N, M, K)
        if safe_zone_count > max_safe_zones:
            max_safe_zones = safe_zone_count
            optimal_K = K
    
    return optimal_K, max_safe_zones

# 입력 처리
optimal_K, max_safe_zones = find_max_safe_zones(n, m, graph)
print(optimal_K, max_safe_zones)