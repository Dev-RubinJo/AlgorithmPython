def dp():
    for i in range(1, len(tri)):
        if i == 1:
            for j in range(2):
                tri[i][j] += tri[0][0]
        elif i > 1:
            for j in range(len(tri[i])):
                if j == 0:
                    tri[i][j] += tri[i - 1][j]
                elif j == len(tri[i]) - 1:
                    tri[i][j] += tri[i - 1][j - 1]
                else:
                    tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])

n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

dp()
print(max(tri[n - 1]))
