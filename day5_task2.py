import util

class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
    
    def __str__(self):
        return "{ \"start\": " + str(self.start) + ", \"end\": " + str(self.end) + "}"
    
    def __repr__(self):
        return self.__str__()


lines = util.read_lines(False)
res = 0
ranges = []
for line in lines:
    if not line:
        break
    range_split = line.split("-")
    ranges.append(Range(int(range_split[0]), int(range_split[1])))

i = 0
while i < len(ranges):
    current_range = ranges[i]
    merged = False
    for j in range(len(ranges)):
        if i == j:
            continue
        ran = ranges[j]
        if current_range.start >= ran.start and current_range.start <= ran.end or current_range.end >= ran.start and current_range.end <= ran.end:
            ran.start = min(ran.start, current_range.start)
            ran.end = max(ran.end, current_range.end)
            del ranges[i]
            merged = True
            break
    if not merged:
        i += 1

for ran in ranges:
    res += ran.end - ran.start + 1

print(res)