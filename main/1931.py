import sys
input = sys.stdin.readline

N = int(input())

conference_room = []
rooms = 0
end_time = 0

for i in range(N):
    start, end = map(int, input().split())
    conference_room.append([start, end])
conference_room.sort(key=lambda x: (x[1], x[0]), reverse=False)

for meeting in conference_room:
    if meeting[0] >= end_time:
        rooms += 1
        end_time = meeting[1]

print(rooms)
