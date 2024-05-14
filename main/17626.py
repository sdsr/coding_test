import sys

input = sys.stdin.readline


def min_four_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, int(n ** 0.5) + 1):
        square = i ** 2
        for j in range(square, n + 1):
            dp[j] = min(dp[j], dp[j - square] + 1)
    return dp[n]


print(min_four_squares(int(input())))
