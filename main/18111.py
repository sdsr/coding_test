import sys
import statistics

N, M, B = map(int, input().split())
ground = []
minimum_time = [sys.maxsize, 0]

for i in range(N):
    ground.extend(list(map(int, input().split())))

mode = statistics.mode(ground)
highest = max(ground)

for i in range(highest + 1):
    my_time = 0
    bag = B

    for j in range(len(ground)):
        if ground[j] - mode > 0:
            my_time += 2
        elif ground[j] - mode < 0:
            my_time += 1
            bag -= 1
    if my_time < minimum_time[0] and bag > -1:
        minimum_time = [my_time, max(ground)]

    my_time = 0
    bag = B

    if mode + i <= highest and i > 0:
        for j in range(len(ground)):
            if ground[j] - (mode + i) > 0:
                my_time += 2
            elif ground[j] - (mode + i) < 0:
                my_time += 1
                bag -= 1
        if my_time < minimum_time[0] and bag > -1:
            minimum_time = [my_time, mode + i]

        my_time = 0
        bag = B

    if mode - i >= 0 and i > 0:
        for j in range(len(ground)):
            if ground[j] - (mode - i) > 0:
                my_time += 2
            elif ground[j] - (mode - i) < 0:

                my_time += 1
                bag -= 1
        if my_time < minimum_time[0] and bag > -1:
            minimum_time = [my_time, mode - i]

print(minimum_time[0], minimum_time[1])
