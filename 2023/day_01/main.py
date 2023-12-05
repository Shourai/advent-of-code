import re

# def main():
#     total = 0
#     left_value: int
#     right_value: int
#
#     with open("./input", "r") as file:
#         lines = file.read().splitlines()
#
#     list_of_lines = []
#     for line in lines:
#         list_of_lines.append([*line])
#
#     for line in list_of_lines:
#         for char in line:
#             if char.isnumeric():
#                 left_value = char
#                 break
#         for char in reversed(line):
#             if char.isnumeric():
#                 right_value = char
#                 break
#         total += int(left_value + right_value)
# print(total)


def part1():
    total: int = 0

    with open("./input", "r") as file:
        lines = file.read().splitlines()

    for line in lines:
        x = re.findall(r"\d", line)
        left_value = x[0]
        right_value = x[-1]
        total += int(left_value + right_value)

    print(total)


def part2():
    total: int = 0
    numbers: dict[str, str] = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }

    numbers_rev: dict[str, str] = {
        "eno": "1",
        "owt": "2",
        "eerht": "3",
        "ruof": "4",
        "evif": "5",
        "xis": "6",
        "neves": "7",
        "thgie": "8",
        "enin": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }

    with open("./test_input_p2", "r") as file:
        lines = file.read().splitlines()

    for line in lines:
        # find numbers from the left side
        unique_spans = set()
        for num in numbers.keys():
            x = re.search(num, line)
            if x is not None:
                unique_spans.add(x.span())
        y = re.search(r"\d", line)
        if y is not None:
            unique_spans.add(y.span())
        unique_spans = list(sorted(unique_spans))
        left_value = numbers[line[unique_spans[0][0]:unique_spans[0][1]]]

        # print(left_value)

        # find numbers from the right side
        unique_spans_right = set()
        for num in numbers.keys():
            x = re.search(num[::-1], line[::-1])
            if x is not None:
                unique_spans_right.add(x.span())
        y = re.search(r"\d", line[::-1])
        if y is not None:
            unique_spans_right.add(y.span())
        unique_spans_right = list(sorted(unique_spans_right))
        # print(unique_spans_right)
        right_value = numbers_rev[line[::-1][unique_spans_right[0][0]:unique_spans_right[0][1]]]
        # print(right_value)

        # print(left_value, right_value)
        total += int(left_value + right_value)
        # print("\n")

    print(total)


if __name__ == "__main__":
    # part1()
    part2()
