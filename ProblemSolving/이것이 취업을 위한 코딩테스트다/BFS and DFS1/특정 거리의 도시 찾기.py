from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0
queue = deque([x])
while queue:
    now = queue.popleft()
    for node in graph[now]:
        if distance[node] == -1:
            distance[node] = distance[now] + 1
            queue.append(node)
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)