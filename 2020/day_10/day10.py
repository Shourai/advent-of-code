with open('day10-input') as file:
    data = file.read().split()
    data = [int(i) for i in data]

data = sorted(data)


def part1():
    oneJoltDifference = 0
    threeJoltDifference = 0

    for jolt in range(len(data) - 1):
        if data[jolt+1] - data[jolt] == 1:
            oneJoltDifference += 1
        elif data[jolt+1] - data[jolt] == 3:
            threeJoltDifference += 1

    print(f"one jolts: {oneJoltDifference + 1}",
          f"three jolts: {threeJoltDifference + 1}")


def part2(data):

    # prepend 0 and append device jolt which is the last adapter +3
    data.insert(0, 0)
    data.append(data[-1] + 3)

    PossibleRoutes = {str(data[-1]): 1}

    for i in range(len(data)-2, -1, -1):
        PossibleRoutes[str(data[i])] = 0
        for gap in [3, 2, 1]:
            if data[i] + gap in data:
                PossibleRoutes[str(data[i])
                               ] += PossibleRoutes[str(data[i] + gap)]

    return PossibleRoutes


print(part2(data))
