import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin = []

while N:
    N -= 1
    coin.append(int(input()))

i = len(coin) - 1
count = 0
while K > 0 and i >= 0:
    if coin[i] <= K:
        count += K // coin[i]
        K %= coin[i]
    i -= 1

print(count)
