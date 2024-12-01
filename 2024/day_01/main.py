from collections import Counter

with open("./testinput", "r") as f:
    left_list = []
    right_list = []

    data = f.readlines()

    for line in data:
        a = line.split()
        left_list.append(int(a[0]))
        right_list.append(int(a[1]))


def part1():
    left_list.sort()
    right_list.sort()
    count = 0

    for i, j in zip(left_list, right_list):
        count += abs(i - j)
    print(count)


def part2():
    count = 0

    # Create a dictionary counter

    # d = {}
    # for i in right_list:
    #     if i in d:
    #         d[i] += 1
    #     else:
    #         d[i] = 1

    d = Counter(right_list)

    for j in left_list:
        if j in d:
            count += j * d[j]
    print(count)


if __name__ == "__main__":
    part1()
    part2()
