import sys
from collections import deque

input = sys.stdin.readline

snake = {}
ladder = {}
check = [False] * 101
Q = deque()
Q.append(1)

N, M = map(int, input().split())

for i in range(N):
    start, end = list(map(int, input().split()))
    ladder[start] = end

for j in range(M):
    start, end = list(map(int, input().split()))
    ladder[start] = end

count = 0
continue_loop = True
while continue_loop:
    length = len(Q)
    for _ in range(length):
        where = Q.popleft()

        if where == 100:
            print(count)
            continue_loop = False
            break

        for i in range(1, 7):
            new_where = where + i

            if new_where <= 100 and check[new_where] is False:
                check[new_where] = True

                if new_where in ladder.keys():
                    check[ladder[new_where]] = True
                    Q.append(ladder[new_where])
                elif new_where in snake.keys():
                    check[snake[new_where]] = True
                    Q.append(snake[new_where])
                else:
                    Q.append(new_where)
    count += 1
