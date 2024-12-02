with open("./testinput") as f:
    data = []
    for line in f:
        data.append([int(i) for i in line.split()])


def part1():
    safe_counter = 0
    for report in data:
        d = []
        for i in range(len(report) - 1):
            d.append(report[i] - report[i + 1])
        if all(i < 0 for i in d) or all(i > 0 for i in d):
            if all(1 <= abs(i) <= 3 for i in d):
                safe_counter += 1
    print(safe_counter)


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
