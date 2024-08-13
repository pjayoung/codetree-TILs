'''
n*m 좌측 상단 시작 -> 우측 하단 탈출
상하좌우 인접한 칸으로 이동 가능
뱀이 있는 경우 이동 불가능 (0)
'''
from collections import deque

order = 0
q = deque()

n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def push(x,y):
    global order
    visited[x][y] = True
    q.append((x,y))
    if x == n-1 and y == m-1:
        order += 1

def can_go(x,y):
    if not (0<=x<n and 0<= y<m):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] == 0:
        return False
    return True

def BFS():
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    while q:
        x,y = q.popleft()
        for i,j in zip(dx, dy):
            nx, ny = x+i, y+j

            if can_go(nx,ny):
                push(nx,ny)

push(0,0)
BFS()
if order > 0:
    print(1)
else:
    print(0)