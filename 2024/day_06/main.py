import numpy as np
import pprint
import copy

with open("./input", "r") as f:
    m = [["Y"] + list(x)[:-1] + ["Y"] for x in f]

padding = [len(m[0]) * ["Y"]]

m = padding + m + padding
# pprint.pprint(m)

n = copy.deepcopy(m)
print("\n")


def rotate(m):
    return np.rot90(m, k=1)


def walk(m):
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == "^":
                for i in range(1, len(m)):
                    if m[y - i][x] == "Y":
                        return True
                    elif not m[y - i][x] == "#":
                        m[y - i][x] = "^"
                        m[y - i + 1][x] = "X"
                    else:
                        break


def walk_with_obstacle(m, obstacle):
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == "^":
                for i in range(1, len(m)):
                    if m[y - i][x] == "Y":
                        print("Reached edge")
                        return True, 0
                    if not (m[y - i][x] == "#" or m[y - i][x] == "O"):
                        m[y - i][x] = "^"
                        m[y - i + 1][x] = "X"
                        if (y - i, x) not in obstacle:
                            obstacle[(y - i, x)] = 1
                        else:
                            obstacle[(y - i, x)] += 1
                    else:
                        break
    return False, obstacle


def count_visited(m):
    count = 0
    for i in m:
        for j in i:
            if j == "X":
                count += 1
    # pprint.pprint(m)
    print(count + 1)


def part2():
    pass


if __name__ == "__main__":
    # Part 1
    rotations = 0
    finished = False
    while not finished:
        finished = walk(m)
        m = rotate(m)
        rotations += 1
    count_visited(m)

    # Rotate to right direction
    print("rotations: ", rotations)
    r = rotations % 4
    for _ in range(4 - r):
        m = rotate(m)

    # find all visited coordinates
    record_coords = set()
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == "X" or m[y][x] == "^":
                record_coords.add((y, x))
    print(record_coords)

    # Part 2

    # Remove starting coordinate
    starting_coord = None
    for y in range(len(n)):
        for x in range(len(n[y])):
            if n[y][x] == "^":
                starting_coord = (y, x)
                record_coords.remove((y, x))

    count = 0

    for coord in record_coords:
        # print(coord)
        y, x = coord
        newmap = copy.deepcopy(n)
        newmap[y][x] = "O"
        # pprint.pprint(newmap)
        finished = False
        obstacle = {starting_coord: 1}
        while not finished:
            if obstacle == 0:
                continue
            if max(obstacle.values()) > 4:
                count += 1
                break
            finished, obstacle = walk_with_obstacle(newmap, obstacle)
            newmap = rotate(newmap)
    print(count)

    # y,x = (4,9)
    # newmap = copy.deepcopy(n)
    # newmap[y][x] = "O"
    # # pprint.pprint(newmap)
    # finished = False
    # obstacle = {starting_coord: 1}
    # while not finished:
    #     if obstacle == 0:
    #         continue
    #     if max(obstacle.values()) > 4:
    #         count += 1
    #         break
    #     finished, obstacle = walk_with_obstacle(newmap, obstacle)
    #     newmap = rotate(newmap)
    # pprint.pprint(newmap)
    # print(obstacle)
    # print(count)
