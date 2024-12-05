with open("./input", "r") as f:
    data = [[".", ".", "."] + list(x)[:-1] + [".", ".", "."] for x in f.readlines()]

extra = len(data[0]) * ["."]

data = 3 * [extra] + data + 3 * [extra]


def part1():
    mas_list = ["M", "A", "S"]
    occurances = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "X":
                if [data[y][x + 1], data[y][x + 2], data[y][x + 3]] == mas_list:
                    occurances += 1
                if [data[y][x - 1], data[y][x - 2], data[y][x - 3]] == mas_list:
                    occurances += 1
                if [data[y + 1][x], data[y + 2][x], data[y + 3][x]] == mas_list:
                    occurances += 1
                if [data[y - 1][x], data[y - 2][x], data[y - 3][x]] == mas_list:
                    occurances += 1
                if [
                    data[y + 1][x + 1],
                    data[y + 2][x + 2],
                    data[y + 3][x + 3],
                ] == mas_list:
                    occurances += 1
                if [
                    data[y - 1][x + 1],
                    data[y - 2][x + 2],
                    data[y - 3][x + 3],
                ] == mas_list:
                    occurances += 1
                if [
                    data[y + 1][x - 1],
                    data[y + 2][x - 2],
                    data[y + 3][x - 3],
                ] == mas_list:
                    occurances += 1
                if [
                    data[y - 1][x - 1],
                    data[y - 2][x - 2],
                    data[y - 3][x - 3],
                ] == mas_list:
                    occurances += 1
    print(occurances)


def part2():
    occurances = 0
    possibilities = [
        ["M", "M", "S", "S"],
        ["M", "S", "M", "S"],
        ["S", "S", "M", "M"],
        ["S", "M", "S", "M"],
    ]

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "A":
                for p in possibilities:
                    # Check SW, NW, SE, NE
                    if [
                        data[y - 1][x - 1],
                        data[y + 1][x - 1],
                        data[y - 1][x + 1],
                        data[y + 1][x + 1],
                    ] == p:
                        occurances += 1
    print(occurances)


if __name__ == "__main__":
    part1()
    part2()
