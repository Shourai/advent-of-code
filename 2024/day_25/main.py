keys = []
locks = []

line_count = 0

is_lock = False

with open("./input") as f:
    schematic = 5 * [-1]
    for line in f:
        line = line.strip()

        if line_count == 0:
            if all(i == "#" for i in line):
                is_lock = True
            else:
                is_lock = False
        line_count += 1

        for i in range(len(line)):
            if line[i] == "#":
                schematic[i] += 1

        if not line:
            if is_lock:
                locks.append(schematic)
            else:
                keys.append(schematic)
            schematic = 5 * [-1]  # Reset schematic
            line_count = 0


fit_count = 0
for lock in locks:
    for key in keys:
        overlap = list(sum(x) for x in zip(lock, key))
        if all(i < 6 for i in overlap):
            fit_count += 1
print(fit_count)
