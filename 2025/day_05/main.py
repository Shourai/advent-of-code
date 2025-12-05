with open("./input", "r") as file:
    input = [line.strip() for line in file.readlines()]


def part1():
    id_ranges = []
    ids = []
    for i in input:
        if i and "-" in i:
            id_ranges.append(i)
        elif i:
            ids.append(i)
    validIDs = []
    for id in ids:
        for idRange in id_ranges:
            left_part = int(idRange.split("-")[0])
            right_part = int(idRange.split("-")[1])
            id = int(id)
            if id >= left_part and id <= right_part:
                # print(f"{id} is fresh, it falls within {left_part, right_part}")
                validIDs.append(id)

    print(len(set(validIDs)))


def part2():
    id_ranges = []
    for i in input:
        if i and "-" in i:
            left, right = i.split("-")
            id_ranges.append([int(left), int(right)])

    id_ranges = sorted(id_ranges)

    merged_interval = []

    for idRange in id_ranges:
        lower_interval = idRange[0]
        upper_interval = idRange[1]
        while merged_interval and merged_interval[-1][1] >= idRange[0]:
            popped = merged_interval.pop()
            lower_interval = min(popped[0], idRange[0])
            upper_interval = max(popped[1], idRange[1])
        merged_interval.append([lower_interval, upper_interval])

    count = 0
    for interval in merged_interval:
        count += interval[1] - interval[0] + 1
    print(count)


part2()
