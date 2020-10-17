n = int(input())
array = [0 for _ in range(10)]
while n > 0:
    array[int(n % 10)] += 1
    n = n // 10
for i in range(10, -1, -1):
    for _ in range(array[i - 1]):
        print(i - 1, end = '')