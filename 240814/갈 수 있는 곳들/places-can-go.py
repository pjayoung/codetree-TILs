'''
0,1로 이루어진 n*n 격자
k개의 시작점으로부터 상하좌우 인접한 곳으로만 이동 가능
도달 가능한 칸의 수를 구하는 프로그램
0 -> 이동 가능 / 1 -> 이동 불가능
'''

from collections import deque

n, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
rc_list = [list(map(int,input().split())) for _ in range(k)]
# r행, c열 위치가 시작점 중 하나임을 의미 (r,c는 파이썬 인덱스보다 +1 상태)
for i in rc_list:
    i[0], i[1] = i[0]-1, i[1]-1
# idx에 맞춰 수정

order = 0
q = deque()

def push(x,y):
    global order
    order += 1
    visited[x][y] = True
    q.append((x,y))

def can_go(x,y):
    if not (0<=x<n and 0<= y<n):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] == 1:
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

for i in rc_list:
    if not visited[i[0]][i[1]]:
        push(i[0],i[1])
        BFS()

print(order)