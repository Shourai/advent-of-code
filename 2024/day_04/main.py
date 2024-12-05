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
                # E
                if [data[y][x + 1], data[y][x + 2], data[y][x + 3]] == mas_list:
                    occurances += 1
                # W
                if [data[y][x - 1], data[y][x - 2], data[y][x - 3]] == mas_list:
                    occurances += 1
                # N
                if [data[y + 1][x], data[y + 2][x], data[y + 3][x]] == mas_list:
                    occurances += 1
                # S
                if [data[y - 1][x], data[y - 2][x], data[y - 3][x]] == mas_list:
                    occurances += 1
                # NE
                if [
                    data[y + 1][x + 1],
                    data[y + 2][x + 2],
                    data[y + 3][x + 3],
                ] == mas_list:
                    occurances += 1
                # SE
                if [
                    data[y - 1][x + 1],
                    data[y - 2][x + 2],
                    data[y - 3][x + 3],
                ] == mas_list:
                    occurances += 1
                # NW
                if [
                    data[y + 1][x - 1],
                    data[y + 2][x - 2],
                    data[y + 3][x - 3],
                ] == mas_list:
                    occurances += 1
                # SW
                if [
                    data[y - 1][x - 1],
                    data[y - 2][x - 2],
                    data[y - 3][x - 3],
                ] == mas_list:
                    occurances += 1
    print(occurances)


def part2():
    """
    There are 4 configurations of the X-MAS
    M.S    M.M    S.M    S.S
    .A. -> .A. -> .A. -> .A.
    M.S    S.S    S.M    M.M
    """
    occurances = 0
    possibilities = [
        # NW , NE , SE, SW
        ["M", "S", "M", "S"],
        ["M", "M", "S", "S"],
        ["S", "M", "S", "M"],
        ["S", "S", "M", "M"],
    ]

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "A":
                for p in possibilities:
                    # Check NW,NE,SW,SE
                    if [
                        data[y + 1][x - 1],
                        data[y + 1][x + 1],
                        data[y - 1][x - 1],
                        data[y - 1][x + 1],
                    ] == p:
                        occurances += 1
    print(occurances)


if __name__ == "__main__":
    part1()
    part2()
