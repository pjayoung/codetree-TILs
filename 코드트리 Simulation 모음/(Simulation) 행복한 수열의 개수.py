'''
n*n 크기의 격자
행복한 수열 : "연속하여" m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
-> 2n개의 수열 중 행복한 수열의 개수 출력

'''

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# [[],[],[]]

ans = 0

# 열 기준
for col in range(n):
    last = 0
    col_num = 1
    update = 0
    for row in range(n):
        if grid[row][col] == last:
            col_num += 1
            last = grid[row][col]
        else:
            update = max(col_num, update)
            col_num = 1
            last = grid[row][col]
        update = max(col_num, update)
    if update >= m:
        ans += 1

# 행 기준
for row in grid:
    last = 0
    row_num = 1
    update = 0
    for i in row:
        if i == last:
            row_num += 1
            last = i
        else:
            update = max(row_num, update)
            row_num = 1
            last = i
        update = max(row_num, update)
    if update >= m:
        ans += 1

print(ans)