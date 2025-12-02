with open("./input", "r") as file:
    input = file.read().strip().split(",")


def part1():
    invalidIDs = []

    for prodRange in input:
        lower = prodRange.split("-")[0]
        upper = prodRange.split("-")[1]

        # Check if length is odd and adjust accordingly
        # for example the range 95-115 should only check between 95-100 since 115 has an odd length

        # If both lower and upper are odd, just skip them
        if len(lower) % 2 != 0 and len(upper) % 2 != 0:
            continue

        elif len(lower) % 2 != 0:
            lower = 10 ** (len(upper) - 1)

        elif len(upper) % 2 != 0:
            upper = 10 ** len(str(lower))

        # print(lower, upper)
        mid = len(str(lower)) // 2

        for i in range(int(lower), int(upper) + 1):
            if str(i)[mid:] == str(i)[:mid]:
                invalidIDs.append(int(i))

    print(sum(invalidIDs))


def part2():
    from itertools import batched

    invalidIDs = []

    for prodRange in input:
        lower = prodRange.split("-")[0]
        upper = prodRange.split("-")[1]

        for i in range(int(lower), int(upper) + 1):
            mid = len(str(i)) // 2
            for j in range(1, mid + 1):
                if len(set(list(batched(str(i), j)))) == 1:
                    invalidIDs.append(i)

    print(sum(set(invalidIDs)))


part2()
