import sys
input = sys.stdin.readline

def solution9465():
    tc = int(input().rstrip())

    for _ in range(tc):
        n = int(input().rstrip())
        stickers = []
        dp = []

        for _ in range(2):
            stickers.append(list(map(int, input().rstrip().split())))
            dp.append([-1 for _ in range(n)])

        for i in range(n):
            if i == 0:
                dp[0][i] = stickers[0][i]
                dp[1][i] = stickers[1][i]
            if i == 1:
                dp[1][i] = dp[0][i - 1] + stickers[1][i]
                dp[0][i] = dp[1][i - 1] + stickers[0][i]
            if i >= 2:
                first_row_first = dp[1][i - 1] + stickers[0][i]
                first_row_second = max(dp[0][i - 2], dp[1][i - 2]) + stickers[0][i]

                dp[0][i] = max(first_row_first, first_row_second)

                second_row_first = dp[0][i - 1] + stickers[1][i]
                second_row_second = max(dp[0][i - 2], dp[1][i - 2]) + stickers[1][i]

                dp[1][i] = max(second_row_first, second_row_second)

        print(max(dp[0][n - 1], dp[1][n - 1]))

solution9465()