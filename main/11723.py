import sys

input = sys.stdin.readline

S = []
n = int(input())
for i in range(n):
    func = list(map(str, input().split()))
    print(func)
    if func[0] == "add":
        if func[1] not in S:
            S.append(func[1])
    elif func[0] == "remove" and func[1] in S:
        S.remove(func[1])
    elif func[0] == "check":
        if func[1] in S:
            print(1)
        else:
            print(0)
    elif func[0] == "toggle":
        if func[1] in S:
            S.remove(func[1])
        else:
            S.append(func[1])
    elif func[0] == "all":
        S = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    elif func[0] == "empty":
        S = []
    print(S)

