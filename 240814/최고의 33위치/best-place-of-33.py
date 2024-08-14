'''
동전 있으면 1, 없으면 0
3*3 크기의 격자를 적절하게 잘 잡아서 해당 범위 안에 들어있는 동전의 개수를 최대로 하는 프로그램
'''

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def get_num(row_s, row_e, col_s, col_e):
    num = 0
    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            num += grid[row][col]
    return num

max_coin = 0
#완전 탐색 시작
for row in range(n):
    if row+2 >= n:
        continue
    for col in range(n):
        if col+2 >= n:
            continue
        num = get_num(row, row+2, col, col+2)
        max_coin = max(max_coin, num)
print(max_coin)