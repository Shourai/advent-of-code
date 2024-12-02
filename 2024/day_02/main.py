with open("./input") as f:
    data = []
    for line in f:
        data.append([int(i) for i in line.split()])


def part1():
    increasing_order = []
    decreasing_order = []
    safe_counter = 0

    for lvl in data:
        if all(lvl[i] < lvl[i + 1] for i in range(len(lvl) - 1)):
            increasing_order.append(lvl)
        elif all(lvl[i] > lvl[i + 1] for i in range(len(lvl) - 1)):
            decreasing_order.append(lvl)
    for lvl in increasing_order:
        if all((lvl[i + 1] - lvl[i]) in range(1, 4) for i in range(len(lvl) - 1)):
            safe_counter += 1
    for lvl in decreasing_order:
        if all((lvl[i] - lvl[i + 1]) in range(1, 4) for i in range(len(lvl) - 1)):
            safe_counter += 1
    print(safe_counter)


def part2():
    safe_counter = 0

    for lvl in data:
        for j in range(len(lvl)):
            dampened = lvl[:j] + lvl[j + 1 :]
            if all(
                (dampened[i + 1] - dampened[i]) in range(1, 4)
                for i in range(len(dampened) - 1)
            ):
                safe_counter += 1
                break
            if all(
                (dampened[i] - dampened[i + 1]) in range(1, 4)
                for i in range(len(dampened) - 1)
            ):
                safe_counter += 1
                break
    print(safe_counter)


if __name__ == "__main__":
    part1()
    part2()
