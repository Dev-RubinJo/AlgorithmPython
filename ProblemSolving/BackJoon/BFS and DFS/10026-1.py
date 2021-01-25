import sys
input = sys.stdin.readline

def dfs(n, arr, visited, x, y, dx, dy, check):
    stack = [(x, y)]
    visited[x][y] = 'V'
    arr[x][y] = 'V'

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == "V":
                continue
            elif arr[nx][ny] != 'V' and arr[nx][ny] == check:
                arr[nx][ny] = 'V'
                visited[nx][ny] = 'V'
                stack.append((nx, ny))
    return

def solution10026():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    rgCount = 0
    notRGCount = 0
    n = int(input().rstrip('\n'))
    arr = [list(input().rstrip('\n')) for _ in range(n)]
    arr2 = [['a' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'G':
                arr2[i][j] = 'R'
            else:
                arr2[i][j] = arr[i][j]

    rgArr = [['a' for _ in range(n)] for _ in range(n)]
    notRGArr = [['a' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 'V':
                rgCount += 1
                dfs(n, arr, rgArr, i, j, dx, dy, arr[i][j])
            if arr2[i][j] != 'V':
                notRGCount += 1
                dfs(n, arr2, notRGArr, i, j, dx, dy, arr2[i][j])

    print(str(rgCount) + " " + str(notRGCount))
    return

solution10026()