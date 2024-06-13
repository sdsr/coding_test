import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    M, N, x, y = map(int, input().split())

    k = x
    while k <= M * N:
        # print(k)
        if (k - y) % N == 0:
            break
        k += M
    if k > M * N:
        k = -1
    print(k)
    # print("-----")
