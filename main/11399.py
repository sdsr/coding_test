import sys

input = sys.stdin.readline

N = int(input())
pi = list(map(int, input().split()))

pi.sort(reverse=True)
count = 0
for i in range(len(pi)):
    count += ((i + 1) * pi[i])

print(count)
