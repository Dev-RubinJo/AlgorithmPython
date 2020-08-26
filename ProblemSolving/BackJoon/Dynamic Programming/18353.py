import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.reverse()
d = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j] + 1)
print(n - max(d))










































# 6 5 3 4 2 3 2 1
# 1 2 3 2 4 3 5 6
















