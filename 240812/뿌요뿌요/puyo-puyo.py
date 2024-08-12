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

num = 1

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


def DFS(x, y, k):
    global num
    # 상하좌우
    dxs, dys = [-1,1,0,0], [0,0,-1,1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        if can_go(nx, ny, k):
            num += 1
            visited[nx][ny] = True
            DFS(nx, ny, k)

def get_zone_num(k):
    global num
    num = 1
    initialize_visited()
    
    for i in range(n):
        for j in range(n):
            if can_go(i, j, k):
                visited[i][j] = True
                DFS(i, j, k)

pup = 0
max_num = 0
for k in range(1, 101):
    get_zone_num(k)
    if num > 4:
        pup+=1
    if num > max_num:
        max_num = num

print(pup, max_num)