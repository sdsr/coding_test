import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

while n:
    n -= 1
    item = int(input())
    if item != 0:
        heapq.heappush(heap, (abs(item), item))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
