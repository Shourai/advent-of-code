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
    lst = []

    line = "818181911112111"

    max_len = 12

    sliding_window_len = len(line) - max_len
    left_pointer = 0
    right_pointer = sliding_window_len

    print(f"pointers {left_pointer, right_pointer}")
    print(f"searching between {line[left_pointer:right_pointer]}")
    max_val = "0"
    index = 0
    for idx in range(len(line[left_pointer:right_pointer])):
        if line[idx + left_pointer] > max_val:
            max_val = line[idx + left_pointer]
            index = idx
            if index == 0:
                left_pointer += 1
            else:
                left_pointer = index
            right_pointer = left_pointer + sliding_window_len

    print(left_pointer, right_pointer)

part2()
