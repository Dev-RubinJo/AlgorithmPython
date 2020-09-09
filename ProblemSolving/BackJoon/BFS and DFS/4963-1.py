import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def dfs(graph, visited, x, y, w, h):
    stack = [(x, y)]
    visited[x][y] = True
    graph[x][y] = 0

    while stack:
        cx, cy = stack.pop()
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w or visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                visited[nx][ny] = True
                stack.append((nx, ny))


while True:
    graph = []
    count = 0
    w, h = map(int, input().rstrip('\n').split())
    if w == 0 and h == 0:
        break
    visited = [[False] * w for _ in range(h)]
    for _ in range(h):
        graph.append(list(map(int, input().rstrip('\n').split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                count += 1
                dfs(graph, visited, i, j, w, h)
    print(count)