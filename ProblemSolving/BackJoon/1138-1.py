n = int(input())
array = list(map(int, input().split()))
line = []

for i in range(len(array) - 1, -1, -1):
    line.insert(array[i], i + 1)
for i in line:
    print(i, end=' ')