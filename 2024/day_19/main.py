from functools import cache
patterns = []
designs = []

with open("./input") as f:
    for line in f:
        if "," in line:
            patterns = line.strip().split(",")
            patterns = [i.strip() for i in patterns]
        else:
            designs.append(line.strip())
    designs = designs[1::]

print(patterns)

@cache
def check_match(design):
    if len(design) == 0:
        return 1

    total = 0

    for pattern in patterns:
        if design.startswith(pattern):
            total+= check_match(design[len(pattern):])
    return total


if __name__ == "__main__":
    count = 0
    total = 0
    for design in designs:
        output = check_match(design)
        total += output
        if output:
            count += 1
    print("part 1: ",count)
    print("part 2: ",total)

