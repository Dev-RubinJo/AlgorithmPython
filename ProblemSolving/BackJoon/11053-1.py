"""
import sys
input = sys.stdin.readline

def solution11053():
    n = int(input().rstrip('\n'))
    a = list(map(int, input().rstrip('\n').split()))
    a.insert(0, 0)
    dp = [0 for _ in range(n + 1)]

    for i in range(n + 1):
        last_index = 0
        if i == 0:
            continue
        for j in range(0, i):
            if a[j] < a[i]:
                if a[last_index] < a[j]:
                    last_index = j
        dp[i] = dp[last_index] + 1
    print(max(dp))

solution11053()
"""
import sys
input = sys.stdin.readline

def solution11053():
    n = int(input().rstrip('\n'))
    a = list(map(int, input().rstrip('\n').split()))
    dp = [0 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and dp[j] > dp[i]:
                dp[i] = dp[j]
        dp[i] += 1
    print(max(dp))

solution11053()