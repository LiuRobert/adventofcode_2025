import util


lines = util.read_lines(False)
res = 0
symbols = []

for line in lines:
    symbols.append(line.split())

for i in range(len(symbols[0])):
    operation = symbols[-1][i]
    result = None
    for j in range(len(symbols) - 1):
        current_num = int(symbols[j][i])
        if result is None:
            result = current_num
        elif operation == "*":
            result *= current_num
        elif operation == "+":
            result += current_num
    res += result

print(res)