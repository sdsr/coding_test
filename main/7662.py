import sys
from collections import deque

input = sys.stdin.readline

Q = deque()
T = int(input())

for _ in range(T):
    Q = deque()
    k = int(input())
    for __ in range(k):
        first, second = input().split()
        if first == 'I':
            Q.append(int(second))
        elif first == 'D' and len(Q) > 0:
            if second == '1':
                Q.remove(max(Q))
            elif second == '-1':
                Q.remove(min(Q))
    if len(Q) == 0:
        print("EMPTY")
    else:
        print(max(Q), min(Q))
