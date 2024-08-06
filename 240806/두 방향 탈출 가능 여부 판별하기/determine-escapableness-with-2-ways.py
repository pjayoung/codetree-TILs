'''
아래, 오른쪽 인접 칸으로만 이동 가능
뱀이 있는 경우 이동 불가능
'''

n, m = map(int, input().split())

grid = [[0 for _ in range(n+2)] for _ in range(n+2)]
for i in range(1, n+1):
    num = list(input().split()) 
    for j in range(m): 
        grid[i][j+1] = int(num[j]) 

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

visitied = [[0 for _ in range(n+1)] for _ in range(n+1)]


def in_range(x,y):
    return 0 <= x and x < m and 0 <= y and y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visitied[x][y] or grid[x][y] == 0:
        return False
    
    return True


def DFS(x,y):
    dxs = [1,0]
    dys = [0,1]
    for dx, dy in zip(dxs, dys):
        n_x, n_y = x+dx, y+dy

        if can_go(n_x,n_y):
            visitied[n_x,n_y] = 1
            DFS(n_x,n_y)

visitied[0][0] = 1
DFS(0,0)

if visitied[n-1][m-2] == 1:
    print(1)
else:
    print(0)