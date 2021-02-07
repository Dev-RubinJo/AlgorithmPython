from collections import deque

def bfs(start, target, relationship, visited):
    count = 0
    queue = deque([[start, count]])
    while queue:
        value = queue.popleft()
        start = value[0]
        count = value[1]
        if start == target:
            return count
        if not visited[start]:
            count += 1
            visited[start] = True
            for person in relationship[start]:
                if not visited[person]:
                    queue.append([person, count])
    return -1

def solution2644():
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    relationship = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        relationship[x].append(y)
        relationship[y].append(x)

    return bfs(a, b, relationship, visited)
print(solution2644())