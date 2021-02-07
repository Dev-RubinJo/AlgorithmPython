def check(x, y, n, dx, dy, visited):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 > nx or nx > n - 1 or 0 > ny or ny > n - 1 or visited[nx][ny]:
            return False
    return True

def calculate(x, y, dx, dy, ground):
    result = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        result += ground[nx][ny]
    return result

def dfs(x, n, cost, count, answer, dx, dy, ground, visited):
    if count == 3:
        answer[0] = min(answer[0], cost)
        return answer
    for i in range(x, n):
        for j in range(1, n):
            if check(i, j, n, dx, dy, visited):
                visited[i][j] = True
                for k in range(4):
                    visited[i + dx[k]][j + dy[k]] = True
                dfs(i, n, cost + calculate(i, j, dx, dy, ground), count + 1, answer, dx, dy, ground, visited)
                visited[i][j] = False
                for k in range(4):
                    visited[i + dx[k]][j + dy[k]] = False

def solution14620():
    n = int(input())
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ground = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    answer = [99999999999]
    answer = dfs(1, n, 0, 0, answer, dx, dy, ground, visited)
    print(answer)
solution14620()