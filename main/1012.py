import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
T = int(input())


def cabbage_counter(i, j):
    global N, M
    if 0 <= i < N and 0 <= j < M and cabbageMap[i][j] == [1, 0]:
        cabbageMap[i][j] = [1, 1]
        cabbage_counter(i, j + 1)  # 오른쪽
        cabbage_counter(i + 1, j)  # 아래
        cabbage_counter(i, j - 1)  # 왼쪽
        cabbage_counter(i - 1, j)  # 위
        return 1
    return 0


for a in range(T):
    count = 0
    cabbageMap = []
    M, N, K = map(int, input().split())
    for i in range(N):
        cabbageList = []
        for j in range(M):
            cabbageList.append([0, 0])
        cabbageMap.append(cabbageList)

    for _ in range(K):
        x, y = map(int, input().split())
        cabbageMap[y][x][0] = 1

    for i in range(N):
        for j in range(M):
            if cabbage_counter(i, j) == 1:
                count += 1
    print(count)
