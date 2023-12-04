def part1():
    with open("./input", "r") as file:
        data = file.readlines()

    total: int = 0
    exponent_factor: int

    for line in data:
        numbers = line.strip().split(": ")[1].split(" | ")

        # List comprehension (might be fastest)
        winning_numbers = [int(x) for x in numbers[0].strip().split()]
        numbers_in_hand = [int(x) for x in numbers[1].strip().split()]

        # or use map() function
        # winning_numbers = list(map(int, numbers[0].strip().split()))
        # numbers_in_hand = list(map(int, numbers[1].strip().split()))
        exponent_factor = 0

        for num in winning_numbers:
            if num in numbers_in_hand:
                exponent_factor += 1

        if not exponent_factor == 0:
            total += 2 ** (exponent_factor - 1)
    print(total)


def part2():
    pass


if __name__ == "__main__":
    part1()
    # part2()
