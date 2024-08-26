import sys

input = sys.stdin.readline


def calc(first_line, second_line):
    len_first_line = len(first_line)
    len_second_line = len(second_line)

    LCS = [[0] * (len_second_line + 1) for _ in range(len_first_line + 1)]

    for i in range(1, len_first_line + 1):
        for j in range(1, len_second_line + 1):
            if first_line[i - 1] == second_line[j - 1]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
            else:
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

    return LCS[len_first_line][len_second_line]


first = input().strip()
second = input().strip()

print(calc(first, second))
