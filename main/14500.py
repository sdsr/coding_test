import sys

input = sys.stdin.readline


def check_max_sum(board, tetromino, x, y):
    try:
        return sum(board[x + dx][y + dy] for dx, dy in tetromino)
    except IndexError:  # 범위를 벗어나는 경우
        return 0


tetrominoes = [
    # 긴 막대
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # 가로
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # 세로

    # 정사각형
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # 2x2

    # 'L' 모양
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # 기본 L
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # 시계 방향으로 90도 회전
    [(0, 0), (0, 1), (1, 0), (2, 0)],  # 180도 회전
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # 시계 방향으로 270도 회전
    [(0, 1), (1, 1), (2, 1), (0, 0)],  # 미러 이미지 L
    [(1, 0), (1, 1), (1, 2), (0, 2)],  # 미러 이미지 90도 회전
    [(2, 0), (0, 1), (1, 1), (2, 1)],  # 미러 이미지 180도 회전
    [(0, 0), (0, 1), (0, 2), (1, 0)],  # 미러 이미지 270도 회전

    # 'ㄱㄴ' 모양
    [(0, 0), (0, 1), (1, 1), (1, 2)],  # ㄱㄴ
    [(0, 1), (1, 1), (1, 0), (2, 0)],  # 90도 회전
    [(0, 1), (0, 0), (1, 0), (1, -1)],  # 180도 회전
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # 270도 회전

    # 'T' 모양
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # 기본 T
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # 90도 회전
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # 180도 회전
    [(1, 0), (0, 1), (1, 1), (2, 1)]  # 270도 회전
]

count = 1
# while True:
graph = []
N, M = map(int, input().split())
for _ in range(N):
    graph.append(list(map(int, input().split())))

max_sum = 0
for i in range(N):
    for j in range(M):
        for tetromino in tetrominoes:
            max_sum = max(max_sum, check_max_sum(graph, tetromino, i, j))

print(max_sum)
count += 1
