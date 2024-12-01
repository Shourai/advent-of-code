with open("./testinput", "r") as f:
    left = []
    right = []

    data = f.readlines()

    for line in data:
        a = line.split()
        left.append(int(a[0]))
        right.append(int(a[1]))


def part1():
    left.sort()
    right.sort()
    count = 0

    for i, j in zip(left, right):
        count += abs(i - j)
    print(count)


def part2():
    count = 0

    for i in left:
        count += i * right.count(i)
    print(count)


if __name__ == "__main__":
    part1()
    part2()
