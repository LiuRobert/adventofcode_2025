import util
import math

class Box:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.connections = []
        self.closest_distance = None
        self.closes_neighbor = None

    def distance(self, box) -> float:
        return math.sqrt(pow(self.x - box.x, 2) + pow(self.y - box.y, 2) + pow(self.z - box.z, 2))
    
    def connect(self, box) -> None:
        self.connections.append(box)
        if (not self in box.connections):
            box.connect(self)
    
    def __str__(self) -> str:
        return f'{{"x": {self.x}, "y": {self.y}, "z": {self.z}}}'


lines = util.read_lines(True)
n_connections = 10
boxes = []
res = 0

for line in lines:
    coords = line.split(",")
    boxes.append(Box(int(coords[0]), int(coords[1]), int(coords[2])))

for box in boxes:
    closest_distance = 999999999999999.99
    closest_neighbor = None
    for neighbor in boxes:
        if box != neighbor:
            distance = box.distance(neighbor)
            if distance < closest_distance:
                closest_distance = distance
                closest_neighbor = neighbor
    box.closest_distance = closest_distance
    box.closes_neighbor = closest_neighbor

for n in range(n_connections):
    next_box: Box
    closest_distance = 9999999999999999.99
    for box in boxes:
        if box.closest_distance < closest_distance and len(box.connections) == 0:
            closest_distance = box.closest_distance
            next_box = box
    next_box.connect(next_box.closes_neighbor)

circuits = []
for box in boxes:
    if box. #TODO make this work