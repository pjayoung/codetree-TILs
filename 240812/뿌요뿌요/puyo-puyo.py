'''
상하좌우로 인접한 칸끼리 같은 숫자 -> 하나의 블럭
블럭 이루는 칸 4개 이상 -> 블럭 터짐

터지게 되는 블럭의 수 + 최대 블럭의 크기
'''

import sys
sys.setrecursionlimit(2500)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def can_go(x,y,k):
    if not (0<=x<n and 0<=y<n):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] != k:
        return False
    return True


def dfs(x, y, k):
    # 상하좌우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    count = 1
    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny, k):
            count += dfs(nx, ny, k)
    return count

pup = 0
max_num = 0
initialize_visited()

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            size = dfs(i, j, grid[i][j])
            if size >=4:
                pup += 1
            max_num = max(size, max_num)

print(pup, max_num)