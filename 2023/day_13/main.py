# pyright: standard
from pprint import pprint

maps = [[]]

with open("./test", "r") as f:
    for line in f:
        if line := line.rstrip():
            maps[-1].append(tuple(line))
        else:
            maps.append([])


def compare(left, right, budget: int):
    for a, b in zip(left, right):
        if a != b:
            budget -= 1
    return budget


def check_map(map):
    total = 0

    for i in range(len(map) - 1):
        if check_full_symmetry(map, i):
            total += i + 1

    return total


def check_full_symmetry(map, start_point) -> bool:
    budget = 0
    top_pointer = start_point
    bot_pointer = start_point + 1

    bot_boundary = len(map) - 1

    top_max_iter = top_pointer
    bot_max_iter = bot_boundary - bot_pointer

    max_iter = min(top_max_iter, bot_max_iter)

    for i in range(0, max_iter + 1):
        budget = compare(map[top_pointer - i], map[bot_pointer + i], budget)
        if budget < 0:
            return False

    return budget == 0


total = 0
for map in maps:
    pprint(map)

    value = check_map(map)
    print(value)
    if value:
        total += (value) * 100
    value = check_map(list(zip(*map)))
    print(value)
    if value:
        total += value
    # pprint(list(zip(*map)))
print(total)
