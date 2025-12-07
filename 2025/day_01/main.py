with open("./input", "r") as file:
    input = [line.strip() for line in file.readlines()]

position = 50
zero_counter = 0

for rotation in input:
    if "L" in rotation:
        left = int(rotation[1::])
        if left > 100 and left % 100 != 0:
            zero_counter += left // 100
            left = left % 100
        if position - left < 0 and position != 0:
            zero_counter += 1
        position = (position - left) % 100
        if position == 0:
            zero_counter += 1

    else:
        right = int(rotation[1::])
        if right > 100 and right % 100 != 0:
            zero_counter += right // 100
            right = right % 100
        if position + right > 100 and position != 0:
            zero_counter += 1
        position = (position + right) % 100
        if position == 0:
            zero_counter += 1

print(zero_counter)
