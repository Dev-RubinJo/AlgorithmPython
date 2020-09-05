import sys
input = sys.stdin.readline
num = int(input())

students = []
for _ in range(num):
    students.append(list(map(int, input().split())))
best = []
for i in range(num):
    best.append(0)
    check = []
    for j in range(5):
        for k in range(num):
            if i == k:
                continue
            if students[k][j] == students[i][j] and k not in check:
                best[i] += 1
                check.append(k)
max = -1
index = -1
for i in range(len(best)):
    if max < best[i]:
        max = best[i]
        index = i

# print(best)
print(index + 1)