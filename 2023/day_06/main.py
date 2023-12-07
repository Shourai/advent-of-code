from functools import reduce

data = open(0).readlines()


def part1():
    time = [int(x) for x in data[0].strip().split()[1:]]
    distance = [int(x) for x in data[1].strip().split()[1:]]

    multiple_way_to_win = []

    for t, d in zip(time, distance):
        count: int = 0
        for t_1 in range(0, t):
            if t * t_1 - t_1**2 > d:
                count += 1
        multiple_way_to_win.append(count)

    print(reduce(lambda x, y: x * y, multiple_way_to_win))


def part2():
    time = int("".join(data[0].strip().split()[1:]))
    distance = int("".join(data[1].strip().split()[1:]))

    count = 0

    for t_1 in range(0, time):
        if time * t_1 - t_1**2 > distance:
            count += 1

    print(count)


if __name__ == "__main__":
    part1()
    part2()
