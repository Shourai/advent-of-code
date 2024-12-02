from collections import Counter

with open("./input", "r") as f:
    data = [x.split() for x in f.readlines()]
    print(data)

with open("./input", "r") as f:
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
    score = 0

    for i, j in zip(left, right):
        score += abs(i - j)
    print(score)


def part2():
    count = Counter(right)
    score = 0

    # for i in left:
    #     score += i * right.count(i)

    for i in left:
        if i in count:
            score += i * count[i]
    print(score)


if __name__ == "__main__":
    part1()
    part2()
