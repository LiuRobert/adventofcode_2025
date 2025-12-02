import util
import math

lines = util.read_lines(False)
res = 0
dial = 50
for line in lines:
    number = int(line[1:])
    if line[0] == "R":
        for i in range(number):
            dial += 1
            if dial == 100:
                dial = 0
                res += 1
    elif line[0] == "L":
        for i in range(number):
            dial -= 1
            if dial == 0:
                res += 1
            elif dial == -1:
                dial = 99
print(res)