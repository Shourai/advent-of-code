with open("./input", "r") as file:
    input = [line.strip() for line in file.readlines()]


def part1():
    lst = []

    for line in input:
        left_pointer = "0"
        left_index = 0
        right_pointer = "0"
        for idx in range(len(line) - 1):
            if line[idx] > left_pointer:
                left_pointer = line[idx]
                left_index = idx

        for idx in range(len(line) - 1, left_index, -1):
            if line[idx] > right_pointer:
                right_pointer = line[idx]

        lst.append(int(left_pointer + right_pointer))

    print(sum(lst))


def part2():
    summation = []

    for line in input:
        stack = []
        k = 12
        skips = len(line) - k

        for digit in line:
            while stack and digit > stack[-1] and skips > 0:
                stack.pop()
                skips -= 1
            stack.append(digit)

        summation.append(int("".join(stack[:k])))
    print(sum(summation))


part2()
