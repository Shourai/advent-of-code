import re

with open("./input", "r") as input:
    input = input.read().splitlines()


class Part1:
    numbers = dict()
    root = ""

    for line in input:
        line = line.split(": ")
        if "root" not in line:
            numbers[line[0]] = line[-1]
        else:
            root = line[-1]

    while any(re.findall(r"[a-z]{4}", root)):
        match = re.findall(r"[a-z]{4}", root)
        for m in match:
            root = root.replace(m, "(" + numbers[m] + ")")

    print("Part 1: ")
    print(eval(root))


class Part2:
    # Since humn only appears once and there is no multiplication
    # between humn humn we can use imaginary numbers
    numbers = dict()
    rootA = ""
    rootB = ""

    for line in input:
        line = line.split(": ")
        if "humn" in line:
            numbers[line[0]] = "1j"
        elif "root" in line:
            rootA = line[-1].split()[0]
            rootB = line[-1].split()[-1]
        else:
            numbers[line[0]] = line[-1]

    while any(re.findall(r"[a-z]{4}", rootA)):
        match = re.findall(r"[a-z]{4}", rootA)
        for m in match:
            rootA = rootA.replace(m, "(" + numbers[m] + ")")

    while any(re.findall(r"[a-z]{4}", rootB)):
        match = re.findall(r"[a-z]{4}", rootB)
        for m in match:
            rootB = rootB.replace(m, "(" + numbers[m] + ")")

    print("Part 2: ")
    print(round((eval(rootB)-eval(rootA).real)/eval(rootA).imag))
    # print(eval(rootA))
    # print(eval(rootB))
