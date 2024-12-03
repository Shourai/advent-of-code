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
    count = 0
    skip = False
    matches = re.findall(r"don\'t\(\)|do\(\)|mul\(\d+,\d+\)", data)
    for i in matches:
        if "don't" in i:
            skip = True
            continue
        elif "do" in i:
            skip = False
            continue
        if skip:
            continue
        else:
            x1, x2 = re.findall(r"\d+", i)
            count += int(x1) * int(x2)
    print(count)


if __name__ == "__main__":
    part1()
    part2()
