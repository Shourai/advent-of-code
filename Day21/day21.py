import re

with open("./input", "r") as input:
    input = input.read().splitlines()


numbers = dict()
root = ""

for line in input:
    line = line.split(": ")
    if "root" not in line:
        numbers[line[0]] = line[-1]
    else:
        root = line[-1]


while any(re.findall(r"[a-z]{4}", root)):
    match = re.findall(r"[a-z]{4}", root)
    for m in match:
        root = root.replace(m, "(" + numbers[m] + ")")

print(eval(root))
