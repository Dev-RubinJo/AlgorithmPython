import sys
input = sys.stdin.readline

n, l, r = map(int, input().rstrip('\n').split())

countries = []
for _ in range(n):
    countries.append(list(map(int, input().rstrip('\n').split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def find_united(x, y, index):
    united = []
    united.append((x, y))
    queue = []
    queue.append((x, y))

    in_united[x][y] = index
    summary = countries[x][y]
    count = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and in_united[nx][ny] == -1:
                if l <= abs(countries[nx][ny] - countries[x][y]) <= r:
                    queue.append((nx, ny))

                    in_united[nx][ny] = index
                    summary += countries[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        countries[i][j] = summary // count

answer = 0
while True:
    in_united = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if in_united[i][j] == -1:
                find_united(i, j, index)
                index += 1
    if index == n * n:
        break
    answer += 1
print(answer)