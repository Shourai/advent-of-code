import numpy as np
import pprint

with open("./input", "r") as f:
    m = [["Y"] + list(x)[:-1] + ["Y"] for x in f]

padding = [len( m[0] ) * ["Y"]]

m = padding + m + padding
# pprint.pprint(m)

print("\n")


def rotate(m):
    return np.rot90(m, k=1)


record_coords = []


def walk(m):
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == "^":
                for i in range(1, len(m)):
                    if m[y-i][x] == "Y":
                        print("Reached edge")
                        part1(m)
                        exit()
                    elif not (m[y - i][x] == "#" or m[y-i][x] == "Y"):
                        m[y - i][x] = "^"
                        m[y - i + 1][x] = "X"
                        record_coords.append((y - i, x))
                    else:
                        break
def part1(m):
    count = 0
    for i in m:
        for j in i:
            if j == "X":
                count += 1
    pprint.pprint(m)
    print(count + 1)


def part2():
    pass


if __name__ == "__main__":
    while True:
        walk(m)
        m = rotate(m)
    pprint.pprint(m)

    part1(m)
    part2()
