import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
numbers = list(map(int, data[2:2+N]))

# 누적 합 배열을 계산
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]

# 질의 처리
output = []
index = 2 + N
for _ in range(M):
    a = int(data[index])
    b = int(data[index + 1])
    index += 2
    # 구간 [a, b]의 합을 계산
    result = prefix_sum[b] - prefix_sum[a - 1]
    output.append(str(result))

# 결과 출력
sys.stdout.write("\n".join(output) + "\n")
