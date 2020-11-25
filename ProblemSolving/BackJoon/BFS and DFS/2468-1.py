import sys
import copy
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input().strip('\n'))
area = []
for _ in range(n):
    area.append(list(map(int, input().strip('\n').split())))

max_island = 1
max_height = max(map(max, area))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, temp):
    temp[x][y] = 0 # 방문표시
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if temp[nx][ny] != 0:
                dfs(nx, ny, temp)


for t in range(1, max_height + 1):
    temp = copy.deepcopy(area)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] <= t:
                temp[i][j] = 0
    count = 0
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] != 0:
                dfs(i, j, temp)
                count += 1
    max_island = max(max_island, count)
print(max_island)
