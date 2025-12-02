import util
import math

line = util.read_lines(False)[0]
ranges = line.split(",")
res = 0

for r in ranges:
    range_start = int(r.split("-")[0])
    range_end = int(r.split("-")[1])
    for i in range(range_start, range_end + 1):
        id = str(i)
        for group_range in range(1, math.floor(len(id)/2) + 1):
            groups = set()
            for j in range(0, len(id), group_range):
                current_group = id[j:j + group_range]
                groups.add(current_group)
            if len(groups) == 1:
                res += i
                break

print(res)