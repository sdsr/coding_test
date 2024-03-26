import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    max_heap = []
    min_heap = []
    exist = {}

    k = int(input())
    for __ in range(k):
        first, second = input().split()
        second = int(second)

        if first == 'I':
            heapq.heappush(max_heap, -second)
            heapq.heappush(min_heap, second)
            exist[second] = exist.get(second, 0) + 1

        elif first == 'D':
            if second == 1:
                while max_heap and exist[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    exist[max_val] -= 1
            elif second == -1:
                while min_heap and exist[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    exist[min_val] -= 1

    while max_heap and exist[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and exist[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")
