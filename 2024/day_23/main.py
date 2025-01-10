from itertools import combinations

d = dict()

with open("./input") as f:
    for line in f:
        left, right = line.strip().split("-")

        if left not in d:
            d[left] = {right}
        else:
            d[left].add(right)
        if right not in d:
            d[right] = {left}
        else:
            d[right].add(left)


another_set = set()
for k, v in d.items():
    for comb in combinations(v, 2):
        left, right = comb
        if right in d[left]:
            # another_set.add(frozenset((k, left, right)))
            another_set.add(tuple(sorted((k, left, right))))

count = 0
for i in another_set:
    if any(j.startswith("t") for j in i):
        count += 1

print(count)
