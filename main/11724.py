import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
checked = [0] * N
graph = [[] for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


def dfs(v):
    global checked
    global graph
    checked[v] = 1
    for i in graph[v]:
        if not checked[i]:
            dfs(i)


count = 0
for i in range(N):
    if not checked[i]:
        dfs(i)
        count += 1

# print(graph)
# print(checked)
print(count)
