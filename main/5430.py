import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    reverse = False
    error = False
    func = input().strip()
    arrSize = int(input())
    input_line = str(input()).strip()
    input_line = input_line.replace('[', '')
    input_line = input_line.replace(']', '')

    arr = deque(input_line.split(','))
    for i in range(len(func)):
        if func[i] == 'R':
            reverse = not reverse
        else:
            if arrSize == 0:
                print("error")
                error = True
                break
            elif reverse:
                arr.pop()
                arrSize -= 1
            elif not reverse:
                arr.popleft()
                arrSize -= 1
    if not error:
        if reverse:
            arr.reverse()
        print("[" + ",".join(arr) + "]")
