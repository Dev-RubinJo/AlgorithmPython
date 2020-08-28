n = int(input())
pair = int(input())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(pair):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


queue = [1]
visited = []

while queue:
    temp = queue.pop()
    visited.append(temp)

    for i in range(len(graph)):
        if graph[temp][i] and i not in visited and i not in queue:
            queue.append(i)
print(len(visited) - 1)
