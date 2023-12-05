total = 0
x = 0

with open('day3-input') as file:
    lines = file.read().splitlines()
    # for line in file:
    #
    #     output = line.strip('\n')

    treeCnt = 0
    x = 0

    for y in range(2, len(lines), 2):
        print(y)
        x = (x + 1) % len(lines[y])

        if lines[y][x] == "#":
            treeCnt += 1

    print("Tree Count: ", treeCnt)

# print(total)
