from collections import deque
import sys

# 재귀 깊이 제한을 늘림 (필요한 경우에만)
# sys.setrecursionlimit(10000)

input = sys.stdin.readline

def bfs(arr, x, y, visited, color):
    n = len(arr)
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_areas(arr):
    n = len(arr)
    visited = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(arr, i, j, visited, arr[i][j])
                count += 1
    return count

# 입력 받기
N = int(input())
arr = [input().strip() for _ in range(N)]

# 원래 배열에 대해 영역 수 세기
original_count = count_areas(arr)

# 'R'을 'G'로 바꾼 배열에 대해 영역 수 세기
rg_arr = [row.replace('R', 'G') for row in arr]
rg_count = count_areas(rg_arr)

print(original_count, rg_count)
