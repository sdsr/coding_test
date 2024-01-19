input_line = input() + '-'
start, end, = 0, 0
count = 0
i = 0
result = ""
# print(len(input_line))
while i < len(input_line):
    temp = ""
    if input_line[i] == '-' or i == len(input_line) - 1:
        if count == 0:
            count = 1
            start = i + 1
            # print("start", i)
            result += input_line[end:start - 1]
        else:
            count = 0
            end = i
            i -= 1
            # print("end", i)
    temp = input_line[start:end]
    if temp != "":
        temp = eval(temp)
        result += '-' + str(temp)
        print(temp)
    print("result", result)
    i += 1

print(eval(result))
