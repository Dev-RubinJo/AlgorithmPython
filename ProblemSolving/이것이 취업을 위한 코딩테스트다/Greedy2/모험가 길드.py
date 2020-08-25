import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

array.sort(reverse=True)
answer = []

while array:
    pivot = array[0]
    temp = []
    for _ in range(pivot):
        temp.append(array[0])
        array.remove(array[0])
    answer.append(temp)
print(len(answer))