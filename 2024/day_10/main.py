with open("./input") as f:
    stones = f.read().split()

# Dictionary holding input variables stone and blink as key
# As value what the stone become

memory = {}


def main(stone, blinks):
    if (stone, blinks) in memory:
        return memory[(stone, blinks)]

    if blinks == 0:
        return 1

    if stone == "0":
        return main("1", blinks - 1)

    if len(stone) % 2 == 0:
        mid = len(stone) // 2
        left, right = (str(int(stone[:mid])), str(int(stone[mid:])))
        left_output = main(left, blinks - 1)
        right_output = main(right, blinks - 1)
        return left_output + right_output

    else:
        memory[(stone, blinks)] = main(str(int(stone) * 2024), blinks - 1)

    return memory[(stone, blinks)]


if __name__ == "__main__":
    # total = 0
    # for stone in stones:
    #     total += main(stone, 75)
    # print(total)
    print(main('125', 10))

