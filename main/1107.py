import sys

N = int(input())
M = int(input())
broken_button = set()
if M != 0:
    broken_button = set(input().split())
move_button = sys.maxsize
now = 100

def not_move():
    if N == 100:
        print(0)
        exit()

def move_one_by_one(input_num):
    return abs(N - input_num)

def move_by_number():
    global broken_button, move_button
    # N의 길이에 따른 범위 설정
    upper_bound = max(1000000, N + 1)
    for i in range(upper_bound):
        temp = str(i)
        if all(char not in broken_button for char in temp):
            button_presses = move_one_by_one(i) + len(temp)
            if move_button > button_presses:
                move_button = button_presses
                # 조기 종료 조건: 현재 숫자가 N보다 크고 버튼 누름 횟수가 이미 최소인 경우
                if i > N and button_presses == len(temp):
                    break

def main():
    not_move()
    move_one = move_one_by_one(now)
    move_by_number()
    print(min(move_one, move_button))

main()
