import sys

input = sys.stdin.readline

M, N = map(int, input().split())

passwords = {}

for i in range(M):
    site, password = map(str, input().split())
    passwords[site] = password

for i in range(N):
    site = input().strip()
    print(passwords[site])
