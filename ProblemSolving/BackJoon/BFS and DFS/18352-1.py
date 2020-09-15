import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().rstrip('\n').split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().rstrip('\n').split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0
queue = deque([x])
while queue:
    index = queue.popleft()
    for i in graph[index]:
        if distance[i] == -1:
            distance[i] = distance[index] + 1
            queue.append(i)

flag = False
for i in range(n + 1):
    if distance[i] == k:
        print(i)
        flag = True
if flag is False:
    print(-1)