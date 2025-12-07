import util

lines = util.read_lines(False)
beams = []
for i in range(len(lines[0])):
    if lines[0][i] == "S":
        beams.append(1)
    else:
        beams.append(0)

for line in lines[1:]:
    for i in range(len(line)):
        if line[i] == "^" and beams[i] > 0:
            beams[i - 1] += beams[i]
            beams[i + 1] += beams[i]
            beams[i] = 0

res = 0
for beam in beams:
    res += beam

print(res)
