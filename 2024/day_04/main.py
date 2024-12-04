with open("./input", "r") as f:
    data = [[".",".",".",". "] + list(x)[:-1] + [".",".",".",". "] for x in f.readlines()]

extra = len(data[0]) * ["."]

data = 4 * extra + data + 4 * [extra] 

def part1():
    occurances = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "X":
                try:
                    if (
                        data[y][x + 1] == "M"
                        and data[y][x + 2] == "A"
                        and data[y][x + 3] == "S"
                    ):
                        occurances += 1
                except:
                    pass
                try:
                    if (
                        data[y][x - 1] == "M"
                        and data[y][x - 2] == "A"
                        and data[y][x - 3] == "S"
                    ):
                        occurances += 1
                except:
                    pass
                try:
                    if (
                        data[y + 1][x] == "M"
                        and data[y + 2][x] == "A"
                        and data[y + 3][x] == "S"
                    ):
                        occurances += 1
                except:
                    pass
                try:
                    if (
                        data[y - 1][x] == "M"
                        and data[y - 2][x] == "A"
                        and data[y - 3][x] == "S"
                    ):
                        occurances += 1
                except:
                    pass
                try:
                    if (
                        data[y + 1][x + 1] == "M"
                        and data[y + 2][x + 2] == "A"
                        and data[y + 3][x + 3] == "S"
                    ):
                        occurances += 1
                except:
                    pass
                try:
                    if (
                        data[y - 1][x + 1] == "M"
                        and data[y - 2][x + 2] == "A"
                        and data[y - 3][x + 3] == "S"
                    ):
                        occurances += 1
                except:
                    pass
                try:
                    if (
                        data[y + 1][x - 1] == "M"
                        and data[y + 2][x - 2] == "A"
                        and data[y + 3][x - 3] == "S"
                    ):
                        occurances += 1
                except:
                    pass
                try:
                    if (
                        data[y - 1][x - 1] == "M"
                        and data[y - 2][x - 2] == "A"
                        and data[y - 3][x - 3] == "S"
                    ):
                        occurances += 1
                except:
                    pass
    print(occurances)


def part2():
    occurances = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "A":
                try:
                    if (
                        data[y-1][x - 1] == "M"
                        and data[y+1][x - 1] == "M"
                        and data[y-1][x + 1] == "S"
                        and data[y+1][x + 1] == "S"
                    ):
                        occurances += 1
                except:
                    pass
                try:
                    if (
                        data[y-1][x - 1] == "M"
                        and data[y+1][x - 1] == "S"
                        and data[y-1][x + 1] == "M"
                        and data[y+1][x + 1] == "S"
                    ):
                        occurances += 1
                except:
                    pass
                try:
                    if (
                        data[y-1][x - 1] == "S"
                        and data[y+1][x - 1] == "S"
                        and data[y-1][x + 1] == "M"
                        and data[y+1][x + 1] == "M"
                    ):
                        occurances += 1
                except:
                    pass
                try:
                    if (
                        data[y-1][x - 1] == "S"
                        and data[y+1][x - 1] == "M"
                        and data[y-1][x + 1] == "S"
                        and data[y+1][x + 1] == "M"
                    ):
                        occurances += 1
                except:
                    pass
    print(occurances)


if __name__ == "__main__":
    part1()
    part2()
