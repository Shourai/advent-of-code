with open("./input", "r") as file:
    input = list(map(int, file.readlines()))


def part1():
    for i in input:
        for j in input:
            if i + j == 2020:
                print(i * j)


def part2():
    for i in input:
        for j in input:
            for k in input:
                if i + j + k == 2020:
                    print(i * j * k)


if __name__ == "__main__":
    part1()
    part2()
