def part1():
    with open("./testinput", "r") as file:
        input = [line.split() for line in file.readlines()]

    columns = {}

    for line in input:
        for idx in range(len(line)):
            if idx not in columns:
                columns[idx] = []
            columns[idx].append(line[idx])

    count = 0

    for col in columns.values():
        count_multiplication = 1
        count_addition = 0
        if col[-1] == "*":
            for i in range(len(col) - 1):
                count_multiplication *= int(col[i])
        elif col[-1] == "+":
            for i in range(len(col) - 1):
                count_addition += int(col[i])
        if count_multiplication != 1:
            count += count_multiplication
        count += count_addition

    print(count)


def part2():
    from pprint import pprint
    import math

    with open("./input", "r") as file:
        input = [list(line.strip("\n")) for line in file]

    transposed = list(map(list, zip(*input)))
    transposed.append(len(transposed[-1]) * [" "])
    pprint(transposed)

    total = 0
    multiplication_list = []
    addition_list = []

    operator = None
    for row in transposed:
        # Skip row if empty
        if all(ch == " " for ch in row):
            print(multiplication_list)
            print(addition_list)
            if multiplication_list:
                total += math.prod(multiplication_list)
                multiplication_list = []
            if addition_list:
                total += sum(addition_list)
                addition_list = []
            continue

        if row[-1] in ("*", "+"):
            operator = row[-1]

        row_len = len(row) - 1
        number = int("".join(row[0:row_len]))

        if operator == "*":
            multiplication_list.append(number)
        if operator == "+":
            addition_list.append(number)

    print(total)


part2()
