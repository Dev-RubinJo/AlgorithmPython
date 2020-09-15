n = int(input())
stairs = []
dp = [0] * (n + 1)
for _ in range(n):
    stairs.append(int(input()))
for i in range(n):
    if i == 0:
        dp[0] = stairs[0]
    elif i == 1:
        dp[1] = max(stairs[1], stairs[1] + dp[0])
    else:
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n - 1])