n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(n)] for _ in range(n)]

def can_go(nx, ny):
    if not (0 <= nx < n and 0 <= ny < n):  # 범위를 먼저 체크합니다.
        return False
    if graph[nx][ny] == 0:  # 벽이면 이동할 수 없습니다.
        return False
    if visited[nx][ny]:  # 이미 방문한 곳이라면 이동할 수 없습니다.
        return False
    return True

def DFS(x, y):
    # 스택을 이용한 DFS
    stack = [(x, y)]
    count = 0  # 마을 내 사람 수를 셀 변수
    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:  # 이미 방문한 경우 스킵
            continue
        visited[cx][cy] = True
        count += 1
        # 상하좌우 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny):
                stack.append((nx, ny))
    return count

villages = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:  # 사람이고 방문하지 않았다면
            num_people = DFS(i, j)
            villages.append(num_people)

villages.sort()
print(len(villages))
for v in villages:
    print(v)