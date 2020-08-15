from collections import deque
n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        now = queue.popleft()
        for i in range(4):
            next_position = [now[0] + dx[i], now[1] + dy[i]]
            if next_position[0] <= -1 or next_position[0] >= n or next_position[1] <= -1 or next_position[1] >= m:
                continue
            if miro[next_position[0]][next_position[1]] == 0 or miro[next_position[0]][next_position[1]] > 1:
                continue
            miro[next_position[0]][next_position[1]] += miro[now[0]][now[1]]

            queue.append(next_position)
bfs(0, 0)
print(miro[n-1][m-1])