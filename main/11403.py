import sys

input = sys.stdin.read


def floyd_warshall(n, graph):
    # 플로이드-와샬 알고리즘을 이용하여 각 노드 쌍의 연결성을 업데이트
    for k in range(n):
        for i in range(n):
            for j in range(n):
                print(graph[i][k], graph[k][j], graph[i][j])
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    return graph


def main():
    # 입력 처리
    data = input().split()
    n = int(data[0])
    graph = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index + n]))
        index += n
        graph.append(row)

    # 플로이드-와샬 알고리즘 적용
    result = floyd_warshall(n, graph)

    # 결과 출력
    for row in result:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()
