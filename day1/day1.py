class Part1:
    with open("./input", "r") as f:
        data = f.read()

    data = data.split()
    data = list(map(int, data))

    increased = 0

    for idx, value in enumerate(data):
        if idx == len(data) - 1:
            break
        if data[idx+1] > data[idx]:
            increased += 1

    print(increased)


class Part2:
    with open("./input", "r") as f:
        data = f.read()

    data = data.split()
    data = list(map(int, data))

    increased = 0

    for idx, value in enumerate(data):
        if idx == len(data) - 3:
            break
        first_sum = sum([data[idx], data[idx+1], data[idx+2]])
        second_sum = sum([data[idx+1], data[idx+2], data[idx+3]])
        if second_sum > first_sum:
            increased += 1

    print(increased)


Part1()
