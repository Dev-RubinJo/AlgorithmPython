import sys
sys.setrecursionlimit(10000)
m, n = map(int, input().split())
travel_map = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(m):
    travel_map.append(list(map(int, input().split())))
dp = [[-1] * n for _ in range(m)]


def dfs(x, y):
    if x == 0 and y == 0:
        dp[0][0] = 1
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            bx = x + dx[i]; by = y + dy[i]
            if bx >= 0 and bx < m and by >= 0 and by < n:
                if travel_map[bx][by] > travel_map[x][y]:
                    dp[x][y] += dfs(bx, by)
    return dp[x][y]

print(dfs(m - 1, n - 1))

# while stack:
    # now = stack.pop()
    # x, y = now[0], now[1]
    # for i in range(4):
    #     nx = x + dx[i]; ny = y + dy[i]
    #     if nx >= 0 and nx < m and ny >= 0 and ny < n:
    #         if travel_map[nx][ny] < travel_map[x][y]:
    #             if dp[nx][ny] == 0:
    #
    #                 dp[nx][ny] = dp[x][y]
    #
    #             else:
    #                 dp[nx][ny] += dp[x][y]
    #             stack.append([nx, ny])

# for i in range(m):
#     for j in range(n):
#         if i == 0 and j == 0:
#             continue
#         for k in range(4):
#             bx = i + dx[k]
#             by = j + dy[k]
#             if bx >= 0 and bx < m and by >= 0 and by < n:
#                 if travel_map[bx][by] > travel_map[i][j] and dp[bx][by] > 0:
#                     dp[i][j] += dp[bx][by]
