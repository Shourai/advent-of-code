with open("./input", "r") as file:
    input = [line.strip() for line in file.readlines()]


def part1():
    splits = len(input[0]) * [0]
    counter = 0
    for line in input:
        for idx, ch in enumerate(line):
            if ch == "S":
                splits[idx] = 1
            if ch == "^":
                if splits[idx] == 1:
                    splits[idx - 1] = 1
                    splits[idx + 1] = 1
                    splits[idx] = 0
                    counter += 1
    print(counter)


part1()


def part2():
    splits = len(input[0]) * [0]
    for line in input:
        for idx, ch in enumerate(line):
            if ch == "S":
                splits[idx] = 1
            if ch == "^":
                if splits[idx] >= 1:
                    splits[idx - 1] += splits[idx]
                    splits[idx + 1] += splits[idx]
                    splits[idx] = 0
    print(sum(splits))


part2()
