input_line = list(map(str, input().split('-')))
input_line2 = []
for i in input_line:
    input_line2.append(i.split('+'))
result = 0
for i in range(len(input_line2)):
    sum = 0
    for j in range(len(input_line2[i])):
        sum += int(input_line2[i][j])
    if i == 0:
        result += sum
    else:
        result -= sum

print(result)

