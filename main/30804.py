n = int(input())
fruits = list(map(int, input().split()))

count = {}
left = 0
max_length = 0

for right in range(n):
    fruit = fruits[right]
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1

    while len(count) > 2:
        count[fruits[left]] -= 1
        if count[fruits[left]] == 0:
            del count[fruits[left]]
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)
