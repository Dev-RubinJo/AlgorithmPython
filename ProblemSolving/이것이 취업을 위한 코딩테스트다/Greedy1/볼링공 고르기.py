n, m = map(int, input().split())
balls = list(map(int, input().split()))

balls.sort()

answer = 0
for i in range(n):
    for j in range(i + 1, n):
        if balls[i] == balls[j]:
            continue
        else:
            answer += 1
print(answer)