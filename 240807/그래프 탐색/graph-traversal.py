n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

start_points = []
end_points = []
for _ in range(m):
    s, e = map(int, input().split())
    start_points.append(s)
    end_points.append(e)

for start, end in zip(start_points, end_points):
    graph[start].append(end)
    graph[end].append(start)

cnt = 0
def DFS(vertex):
    global cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            cnt += 1
            DFS(curr_v)
    return cnt

root_vertex = start_points[1]
visited[root_vertex] = True
print(DFS(root_vertex))