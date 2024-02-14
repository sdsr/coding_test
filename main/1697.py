from collections import deque


def bfs_min_time(N, K):
    # 최대 위치 범위
    MAX_POSITION = 100000
    # 방문 여부와 시간을 기록하는 배열
    visited = [0] * (MAX_POSITION + 1)

    # BFS를 위한 큐 초기화 및 시작 위치 추가
    queue = deque([N])

    while queue:
        # print(queue)
        current_position = queue.popleft()

        # 동생의 위치에 도달한 경우 시간 반환
        if current_position == K:
            return visited[current_position]

        # 가능한 모든 이동 탐색 (-1, +1, *2)
        for next_position in (current_position - 1, current_position + 1, current_position * 2):
            # 다음 위치가 유효한 범위 내이고 아직 방문하지 않은 경우
            if 0 <= next_position <= MAX_POSITION and not visited[next_position]:
                # 다음 위치를 큐에 추가하고, 시간을 갱신
                visited[next_position] = visited[current_position] + 1
                queue.append(next_position)


def main():
    N, K = map(int, input().split())
    print(bfs_min_time(N, K))


main()
