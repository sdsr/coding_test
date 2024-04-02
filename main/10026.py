import sys

input = sys.stdin.readline

arr = []
arr_check = [[0 for i in range(100)] for j in range(100)]
count = 0
RG_count = 0


def bfs(x, y, color, arr):
    if arr_check[x][y] == 1:
        return False

    if color == arr[x][y]:
        arr_check[x][y] = 1
    else:
        return False

    if x + 1 < N:
        bfs(x + 1, y, color, arr)
    if y + 1 < N:
        bfs(x, y + 1, color, arr)
    if x - 1 >= 0:
        bfs(x - 1, y, color, arr)
    if y - 1 >= 0:
        bfs(x, y - 1, color, arr)


N = int(input())
for _ in range(N):
    arr.append(input().strip())
for x in range(N):
    for y in range(N):
        if bfs(x, y, arr[x][y], arr) != False:
            count += 1

arr2 = [s.replace('R', 'G') for s in arr]
arr_check = [[0 for i in range(N)] for j in range(N)]

for x in range(N):
    for y in range(N):
        if bfs(x, y, arr2[x][y], arr2) != False:
            RG_count += 1

print(count, RG_count)
