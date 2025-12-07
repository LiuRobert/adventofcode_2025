import util


lines = util.read_lines(False)
res = 0
beams = lines[0]

for line in lines[1:]:
    for i in range(len(line)):
        if line[i] == "^" and beams[i] == "S":
            res += 1
            beams = beams[:i - 1] + "S" + beams[i:] 
            beams = beams[:i] + "." + beams[i + 1:]
            beams = beams[:i + 1] + "S" + beams[i + 2:]

print(res)
