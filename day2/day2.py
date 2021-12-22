class Part1:
    with open("./input", "r") as f:
        data = f.read()

    data = data.splitlines()
    data = list(map(lambda x: tuple(x.split()), data))

    x_direction = 0
    y_direction = 0

    for i in data:
        if i[0] == "forward":
            x_direction += int(i[1])
        elif i[0] == "down":
            y_direction += int(i[1])
        elif i[0] == "up":
            y_direction -= int(i[1])

    print(x_direction * y_direction)



class Part2:
    with open("./input", "r") as f:
        data = f.read()

    data = data.splitlines()
    data = list(map(lambda x: tuple(x.split()), data))

    aim = 0
    forward  = 0
    depth = 0

    for i in data:
        if i[0] == "forward":
            forward += int(i[1])
            depth += aim * int(i[1])
        elif i[0] == "down":
            aim += int(i[1])
        elif i[0] == "up":
            aim -= int(i[1])

    print(forward * depth)

Part2()
