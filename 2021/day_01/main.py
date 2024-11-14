def part1(input):
    counter = 0

    for i in range(len(input) - 1):
        if input[i + 1] > input[i]:
            counter += 1
    print(counter)


def part2(input):
    counter = 0

    for i in range(len(input) - 1):
        if sum(input[i + 1 : i + 4]) > sum(input[i : i + 3]):
            counter += 1
    print(counter)


if __name__ == "__main__":
    with open("./input", "r") as f:
        input = list(map(int, f.readlines()))
    part1(input)
    part2(input)
