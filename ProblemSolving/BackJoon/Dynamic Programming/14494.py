import sys

input = sys.stdin.readline

n, m = map(int, input().split())
d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j == 1:
            d[1][1] = 1
            continue
        if i * j != 1:
            d[i][j] = (d[i - 1][j] % int(1e9 + 7) + d[i][j - 1] % int(1e9 + 7) + d[i - 1][j - 1] % int(1e9 + 7)) % int(1e9 + 7)
print(d)