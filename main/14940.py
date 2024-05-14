import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
# n, m = 15, 15
map_map = [list(map(int, input().split())) for _ in range(n)]
# map_map = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
# ]

map_way = [[-1 for _ in range(m)] for _ in range(n)]

target = [0, 0]
for i in range(n):
    for j in range(m):
        if map_map[i][j] == 2:
            target = [i, j]


# def search(pos, count):
#     i, j = pos
#     if i < 0 or i >= m or j < 0 or j >= n:
#         return
#
#     if map_map[i][j] == 0:
#         return
#     if map_way[i][j] != 0 and count != 0 and map_way[i][j] <= count:
#         return
#     map_way[i][j] = count
#
#     search([i - 1, j], count + 1)
#     search([i + 1, j], count + 1)
#     search([i, j - 1], count + 1)
#     search([i, j + 1], count + 1)

def bfs(start):
    queue = deque([start])
    map_way[start[0]][start[1]] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        i, j = queue.popleft()
        current_count = map_way[i][j]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and map_map[ni][nj] != 0:
                if map_way[ni][nj] == -1 or map_way[ni][nj] > current_count + 1:
                    map_way[ni][nj] = current_count + 1
                    queue.append((ni, nj))


bfs(target)

for i in range(n):
    for j in range(m):
        if map_map[i][j] == 0:
            print(0, end=" ")
        else:
            print(map_way[i][j], end=" ")
    print()