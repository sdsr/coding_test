import sys

N, M, B = map(int, input().split())
ground = []
minimum_time = sys.maxsize
max_height = 0

for i in range(N):
    ground.extend(list(map(int, input().split())))

min_height, max_height = min(ground), max(ground)

for i in range(min_height, max_height + 1):
    count_time = 0
    bag = B

    for j in range(len(ground)):
        height_difference = ground[j] - i
        if height_difference > 0:
            count_time += height_difference * 2
            bag += height_difference
        elif height_difference < 0:
            count_time += -height_difference
            bag -= -height_difference
    if (count_time < minimum_time or (count_time == minimum_time and i > max_height)) and bag >= 0:
        minimum_time = count_time
        max_height = i

print(minimum_time, max_height)
