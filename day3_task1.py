import util

def find_biggest_index(line, start_index, max_bigness):
    biggest_number = 0
    biggest_index = 0
    for i in range(start_index, len(line)):
        current_number = int(line[i])
        if current_number < max_bigness and current_number > biggest_number:
            biggest_number = current_number
            biggest_index = i
    return biggest_index


lines = util.read_lines(False)
res = 0

for line in lines:
    biggest_num_index = find_biggest_index(line, 0, 10)
    biggest_num = int(line[biggest_num_index])
    if biggest_num_index == len(line) - 1:
        second_biggest_num = biggest_num
        biggest_num_index = find_biggest_index(line, 0, biggest_num)
        biggest_num = int(line[biggest_num_index])
    else:
        second_biggest_num = line[find_biggest_index(line, biggest_num_index + 1, 10)]
    res += int(str(biggest_num) + str(second_biggest_num))     

print(res)