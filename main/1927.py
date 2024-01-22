import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = []  # 최소 힙
output = []  # 출력을 저장할 리스트

for _ in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            output.append('0')
        else:
            output.append(str(heapq.heappop(heap)))  # 최솟값 추출
    else:
        heapq.heappush(heap, x)  # 요소 삽입

print("\n".join(output))  # 저장된 출력 내용을 한 번에 출력
