n = int(input())
jumps = list(map(int, input().split()))

dp = [1000002 for _ in range(n + 1)]
dp[0] = 0
for i in range(n):
    if jumps[i] != 0:
        for j in range(i + 1, i + 1 + jumps[i]):
            if j > n:
                break
            dp[j] = min(dp[i] + 1, dp[j])
print(dp[n - 1] if dp[n - 1] != 1000002 else -1)