import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    M, N, x, y = map(int, input().split())
    countM, countN = 1, 1
    count = 1

    while countM != x or countN != y:
        if countM >= M and countN >= N:
            count = -1
            break
        if countM < M:
            countM += 1
        else:
            countM = 1

        if countN < N:
            countN += 1
        else:
            countN = 1
        count += 1
        # print(countM, countN, x, y)

    print("count =", count)
