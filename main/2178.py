import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((0, 0))
    list_map[0][0] = 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        if x == N - 1 and y == M - 1:
            return list_map[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and list_map[nx][ny] == 1:
                queue.append((nx, ny))
                list_map[nx][ny] = list_map[x][y] + 1

    return -1

N, M = map(int, input().split())
list_map = []
for i in range(N):
    list_map.append(list(map(int, input().strip())))

# print(list_map)
print(bfs())
