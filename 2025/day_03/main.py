with open("./input", "r") as file:
    input = [line.strip() for line in file.readlines()]


lst = []

for line in input:
    print(f"Now on line {line}")
    left_pointer = 0
    left_index = 0
    right_pointer = 0
    for idx in range(len(line) - 1):
        if int(line[idx]) > left_pointer:
            left_pointer = int(line[idx])
            left_index = idx

    for idx in range(len(line) - 1, left_index, -1):
        if int(line[idx]) > right_pointer:
            right_pointer = int(line[idx])

    lst.append(int(str(left_pointer) + str(right_pointer)))


print(sum(lst))
