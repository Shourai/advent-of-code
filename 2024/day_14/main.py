import re

with open("./input") as f:
    data = f.read()
    data = re.findall(r"-?\d+,-?\d+", data)

quadrants = {"1": [], "2": [], "3": [], "4": []}

width = 101
height = 103
for i in range(0, len(data), 2):
    print("Position: ", data[i])
    print("Velocity: ", data[i + 1])
    print()
    x, y = list(map(int, (data[i].split(","))))
    vx, vy = list(map(int, (data[i + 1].split(","))))

    for _ in range(100):
        x += vx
        x = x % width
        y += vy
        y = y % height
    if x < width // 2 and y < height // 2:
        quadrants["1"].append((x, y))
    elif x > width // 2 and y < height // 2:
        quadrants["2"].append((x, y))
    elif x < width // 2 and y > height // 2:
        quadrants["3"].append((x, y))
    elif x > width // 2 and y > height // 2:
        quadrants["4"].append((x, y))

safety_factor = 1
for i in quadrants.values():
    safety_factor *= len(i)

print(safety_factor)
