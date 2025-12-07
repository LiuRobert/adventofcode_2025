import util

lines = util.read_lines(False)
res = 0

line_values = []
lengths = []
operations = lines[-1].split()

for line in lines[:-1]:
    split_line = line.split()
    for i in range(len(split_line)):
        if len(lengths) < len(split_line):
            lengths.append(len(split_line[i]))
        else:
            lengths[i] = max(lengths[i], len(split_line[i]))

for line in lines[:-1]:
    values = []
    current_char = 0
    for i in range(len(lengths)):
        values.append(line[current_char:current_char + lengths[i]])
        current_char += lengths[i] + 1
    line_values.append(values)

for i in range(len(lengths)):
    result = None
    for j in range(lengths[i] -1, -1, -1):
        num_str = ""
        for line_value in line_values:
            if line_value[i][j] != " ":
                num_str += line_value[i][j]
        num = int(num_str)
        if result is None:
            result = num
        elif operations[i] == "*":
            result *= num
        elif operations[i] == "+":
            result += num
    res += result

print(res)