n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

negative = []
positive = []
answer = 0
for i in array:
    if i <= 0:
        negative.append(i)
    elif i == 1:
        answer += 1
    else:
        positive.append(i)

negative.sort()
positive.sort(reverse=True)

for i in range(0, len(negative), 2):
    if i + 1 < len(negative):
        answer += negative[i] * negative[i + 1]
    else:
        answer += negative[i]
for i in range(0, len(positive), 2):
    if i + 1 < len(positive):
        answer += positive[i] * positive[i + 1]
    else:
        answer += positive[i]
print(answer)