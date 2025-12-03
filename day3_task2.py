import util

def find_biggest_index(line, start_index, max_index):
    biggest_number = 0
    biggest_index = 0
    for i in range(start_index, max_index):
        current_number = int(line[i])
        if  current_number > biggest_number:
            biggest_number = current_number
            biggest_index = i
    return biggest_index


def find_biggest_number(line, n):
    numbers = []
    start_index = 0
    for i in range(n):
        n = n - 1
        index = find_biggest_index(line, start_index, len(line) - n)
        start_index = index + 1
        numbers.append(line[index])
    biggest_number = ""
    for n in numbers:
        biggest_number += n
    return int(biggest_number)


lines = util.read_lines(False)
res = 0
for line in lines:
    res += find_biggest_number(line, 12)  

print(res)