import sys
input = sys.stdin.readline

num = input()
answer = 0
for i in range(len(num) - 1):
    if int(num[i]) == 0 or int(num[i]) == 1:
        answer += int(num[i])
    else:
        if answer == 0:
            answer += int(num[i])
            continue
        answer *= int(num[i])
print(answer)
