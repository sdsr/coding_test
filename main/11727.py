import sys

input = sys.stdin.readline

N = int(input())
DP = [0 for _ in range(N+1)]

DP[0] = 0
DP[1] = 1
DP[2] = 3

def f(n):
    for i in range(3, n+1):
        DP[i] = (DP[i - 1] + 2 * DP[i - 2]) % 10007
    return DP[n]

print(f(N))
print(DP)