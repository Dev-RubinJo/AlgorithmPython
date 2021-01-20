def solution1309():
    n = int(input())
    dp = [3]
    dp.append(7)
    for i in range(2, n):
        dp.append((dp[i - 1] * 2 + dp[i - 2]) % 9901)
    print(dp[n - 1])
solution1309()