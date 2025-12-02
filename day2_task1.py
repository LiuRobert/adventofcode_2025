import util

line = util.read_lines(False)[0]
ranges = line.split(",")
res = 0

for r in ranges:
    range_start = int(r.split("-")[0])
    range_end = int(r.split("-")[1])
    for i in range(range_start, range_end + 1):
        id = str(i)
        if len(id) % 2 == 0:
            n1 = id[:int(len(id)/2)]
            n2 = id[int(len(id)/2):]
            if n1 == n2:
                res += i
print(res)