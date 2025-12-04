import util

def inbounds(lines, y, x):
    return x >= 0 and y >= 0 and x < len(lines[0]) and y < len(lines)

def is_roll(lines, y, x):
    if inbounds(lines, y, x) and lines[y][x] == "@":
        return 1
    return 0

lines = util.read_lines(False)
res = 0

removed_roll = True
while removed_roll:
    removed_roll = False
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "@":
                rolls = is_roll(lines, y - 1, x - 1)
                rolls += is_roll(lines, y - 1, x)
                rolls += is_roll(lines, y - 1, x + 1)
                rolls += is_roll(lines, y, x - 1)
                rolls += is_roll(lines, y, x + 1)
                rolls += is_roll(lines, y + 1, x - 1)
                rolls += is_roll(lines, y + 1, x)
                rolls += is_roll(lines, y + 1, x + 1)
                if rolls < 4:
                    res += 1
                    removed_roll = True
                    lines[y] = lines[y][:x] + "." + lines[y][x + 1:]

print(res)