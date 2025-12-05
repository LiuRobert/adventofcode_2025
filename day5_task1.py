import util


lines = util.read_lines(False)
res = 0
ranges = []
values = []
read_ranges = True
for line in lines:
    if not line:
        read_ranges = False
        continue
    if read_ranges:
        range_split = line.split("-")
        ranges.append({
            "start": int(range_split[0]),
            "end": int(range_split[1]) 
        })
    else:
        values.append(int(line))

for val in values:
    for ran in ranges:
        if val >= ran.get("start") and val <= ran.get("end"):
            res += 1
            break

print(res)