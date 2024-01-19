# 입력 처리
n, m = map(int, input().split())

# 그래프 초기화 (무한대로 초기화, 자기 자신으로의 경로는 0)
graph = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

# 간선 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

# 플로이드-워셜 알고리즘으로 모든 최단 경로 계산
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 케빈 베이컨 수 계산
kevin_bacon = [sum(graph[i]) for i in range(n)]

# 가장 작은 케빈 베이컨 수를 가진 사람 찾기
min_bacon = min(kevin_bacon)
for i in range(n):
    if kevin_bacon[i] == min_bacon:
        print(i + 1)
        break
