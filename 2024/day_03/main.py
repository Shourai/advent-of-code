import re

with open("./input", "r") as f:
    data = f.read()


def part1():
    count = 0
    matches = re.findall(r"(mul\(\d+,\d+\))", data)
    for i in matches:
        x1, x2 = re.findall(r"\d+", i)
        count += int(x1) * int(x2)
    print(count)


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
