from functools import cmp_to_key

with open("./testinput", "r") as f:
    ordering_rules = {}
    pages = []
    for i in f:
        i = i.strip()
        if "|" in i:
            x1, x2 = i.split("|")
            if x1 not in ordering_rules:
                ordering_rules[x1] = [x2]
            else:
                ordering_rules[x1].append(x2)
        if "," in i:
            y = i.split(",")
            pages.append(y)


def part1():
    counter = 0
    for page in pages:
        correct_order = []
        for i in range(len(page) - 1):
            try:
                if page[i + 1] in ordering_rules[page[i]]:
                    correct_order.append(True)
                else:
                    correct_order.append(False)
            except KeyError:
                correct_order.append(False)
        if all(correct_order):
            middle = len(page) // 2
            counter += int(page[middle])

    print(counter)


def compare(a, b):
    print(a, b)
    try:
        if b in ordering_rules[a]:
            return -1
        else:
            return 1
    except KeyError:
        return 0


def part2():
    counter = 0
    for page in pages:
        correct_order = []
        for i in range(len(page) - 1):
            try:
                if page[i + 1] in ordering_rules[page[i]]:
                    correct_order.append(True)
                else:
                    correct_order.append(False)
            except KeyError:
                correct_order.append(False)
        if not all(correct_order):
            sorted_nums = sorted(page, key=cmp_to_key(compare))
            middle = len(sorted_nums) // 2
            counter += int(sorted_nums[middle])

    print(counter)


if __name__ == "__main__":
    part1()
    part2()
