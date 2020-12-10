with open('test-input') as file:
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
    arrangements = 1
    for jolt in range(1, len(data) - 1):
        if data[jolt + 1] - data[jolt] == 1 and data[jolt] - data[jolt - 1] == 1:
            arrangements += 1
            data.pop(jolt)
            print(data)
            part2(data)
            break
        elif data[jolt + 1] - data[jolt] == 2 and data[jolt] - data[jolt - 1] == 2:
            arrangements += 1
            data.pop(jolt)
            print(data)
            part2(data)
            break
    return arrangements


x = part2(data)
print(x)
