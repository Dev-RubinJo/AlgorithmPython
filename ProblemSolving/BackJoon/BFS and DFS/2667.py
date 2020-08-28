n = int(input())
apart = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    apart.append(list(map(int, input().strip())))

def bfs(apart, count, x, y):
    apart[x][y] = 0
    queue = []
    queue.append((x, y))

    while queue:
        x, y = queue.pop()
        for i in range(0, 4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if apart[nx][ny] == 1:
                    count += 1
                    apart[nx][ny] = 0
                    queue.append((nx, ny))
    return count

count = 0
ans = []
for i in range(n):
    for j in range(n):
        if apart[i][j] == 1:
            ans.append(bfs(apart, count + 1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)