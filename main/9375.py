import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    closet = {}
    for __ in range(n):
        item, category = map(str, input().split())
        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1
    result = 1
    for key in closet:
        result *= closet[key] + 1
    print(result - 1)
