'''
아래, 오른쪽 인접 칸으로만 이동 가능
뱀이 있는 경우 이동 불가능
탈출 가능 1, 불가능 0
'''

n, m = map(int, input().split())

grid = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    num = list(input().split()) 
    for j in range(m): 
        grid[i][j] = int(num[j]) 

visitied = [[False for _ in range(m)] for _ in range(n)]


def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visitied[x][y]:
        return False
    if grid[x][y] == 0:
        return False
    
    return True


def DFS(x,y):
    dxs = [1,0]
    dys = [0,1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy

        if can_go(nx,ny):
            visitied[nx][ny] = True
            DFS(nx,ny)

visitied[0][0] = 1
DFS(0,0)

if visitied[n-1][m-1]:
    print(1)
else:
    print(0)