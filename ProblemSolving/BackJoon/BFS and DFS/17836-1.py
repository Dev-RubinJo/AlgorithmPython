from collections import deque
import sys
input = sys.stdin.readline

n, m, t = map(int, input().rstrip('\n').split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip('\n').split())))

get_sword = False
visited = [[-1] * m for _ in range(n)]
visited_after_get_sword = [[-1] * m for _ in range(n)]
start = (0, 0)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque([start])
queue_for_sword = deque([start])
visited[0][0] = 0
visited_after_get_sword[0][0] = 0

while queue:
    px, py = queue.popleft()
    for i in range(4):
        nx, ny = px + dx[i], py + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] != -1:
            continue
        if graph[nx][ny] != 1:
            visited[nx][ny] = visited[px][py] + 1
            queue.append((nx, ny))

while queue_for_sword:
    px, py = queue_for_sword.popleft()
    for i in range(4):
        nx, ny = px + dx[i], py + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited_after_get_sword[nx][ny] != -1:
            continue
        if graph[nx][ny] == 2:
            get_sword = True
            queue_for_sword.clear()
        if get_sword and visited_after_get_sword[nx][ny] == -1:
            visited_after_get_sword[nx][ny] = visited_after_get_sword[px][py] + 1
            queue_for_sword.append((nx, ny))
        elif graph[nx][ny] != 1:
            visited_after_get_sword[nx][ny] = visited_after_get_sword[px][py] + 1
            queue_for_sword.append((nx, ny))

if min(visited[n - 1][m - 1], visited_after_get_sword[n - 1][m - 1]) <= t and visited[n - 1][m - 1] != -1 and visited_after_get_sword[n - 1][m - 1] != -1:
    print(min(visited[n - 1][m - 1], visited_after_get_sword[n - 1][m - 1]))
elif visited[n - 1][m - 1] == -1 or visited[n - 1][m - 1] > t:
    print("Fail")
