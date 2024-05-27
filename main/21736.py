import sys
from collections import deque

# O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다.


input = sys.stdin.readline

N, M = map(int, input().strip().split())
school_map = []
check_map = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    school_map.append(input().strip())

start_point = []
for i in range(N):
    for j in range(M):
        if school_map[i][j] == 'I':
            start_point = [i, j]


def bfs(start_point):
    queue = deque([start_point])
    check_map[start_point[0]][start_point[1]] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    while queue:
        i, j = queue.popleft()
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < M:
                if school_map[ni][nj] != 'X' and not check_map[ni][nj]:
                    queue.append([ni, nj])
                    check_map[ni][nj] = True
                    if school_map[ni][nj] == 'P':
                        count += 1
    return count


result = bfs(start_point)
if result == 0:
    print("TT")
else:
    print(result)
