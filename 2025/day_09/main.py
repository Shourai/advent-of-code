with open("./testinput", "r") as file:
    input = [line.strip() for line in file.readlines()]

coordinates = []
for i in input:
    x, y = i.split(",")
    coordinates.append((int(x), int(y)))


def part1():
    largest = 0
    for i in range(len(coordinates)):
        for j in range(i, len(coordinates)):
            dx = abs(coordinates[i][0] - coordinates[j][0]) + 1
            dy = abs(coordinates[i][1] - coordinates[j][1]) + 1
            if dx * dy > largest:
                largest = dx * dy

    print(largest)


def part2():
    polygon_coords = set()
    sorted_coords = sorted(coordinates, key=lambda x: x[1])
    print(sorted_coords)

    lowest = 999999
    highest = 0
    row_num = 1
    for i in range(0, len(sorted_coords)):
        if i == sorted_coords[i][row_num]:
            polygon_coords.add(sorted_coords[i])
            polygon_coords.add(sorted_coords[i + 1])
            lowest = min(sorted_coords[i][0], sorted_coords[i + 1][0])
            highest = max(sorted_coords[i][0], sorted_coords[i + 1][0])
            i += 1


part2()
