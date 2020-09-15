import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().rstrip('\n').split()))
dp = [0] * n

dp[0] = numbers[0]
for i in range(1, n):
    if dp[i - 1] + numbers[i] > numbers[i]:
        dp[i] = dp[i - 1] + numbers[i]
    else:
        dp[i] = numbers[i]
print(max(dp))
