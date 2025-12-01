import util

lines = util.read_lines(__file__, False)
res = 0
dial = 50
for line in lines:
    if line[0] == "R":
        dial += int(line[1:])
    elif line[0] == "L":
        dial -= int(line[1:])
    dial = dial % 100
    if dial == 0:
        res += 1

print(res)