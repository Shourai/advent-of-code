import re

with open('day16-input') as file:
    data = file.read().splitlines()


trainInfo = []

for line in data:
    if line == "":
        break
    trainInfo.append(line)


nearbyTicketsID = data.index("nearby tickets:")
nearbyTickets = data[nearbyTicketsID+1::]

# print(trainInfo)
trainInfoSet = set()
for numbers in trainInfo:
    x = re.findall(r'(\d+)-(\d+)', numbers)
    for num in x:
        trainInfoSet.update(range(int(num[0]), int(num[1])))


def part1():
    invalidNumber = list()
    for line in nearbyTickets:
        line = line.split(',')
        line = [int(line) for line in line]
        for number in line:
            if number not in trainInfoSet:
                invalidNumber.append(number)
    print(sum(invalidNumber))


def part2():
    validTickets = list()
    for line in nearbyTickets:
        line = line.split(',')
        line = [int(line) for line in line]
        if set(line).issubset(trainInfoSet):
            validTickets.append(line)

    trainInfoDict = dict()
    for info in trainInfo:
        x = re.findall(r'([a-z]+\s?[a-z]+): (\d+)-(\d+) or (\d+)-(\d+)', info)
        y = set()
        y.update(range(int(x[0][1]), int(x[0][2])))
        y.update(range(int(x[0][3]), int(x[0][4])))
        trainInfoDict[x[0][0]] = y

    ticketLen = len(validTickets[0])

    # Create slice of every column
    columns = list()
    for i in range(ticketLen):
        columns.append([x[i] for x in validTickets])

    for idx, column in enumerate(columns):
        for k, v in trainInfoDict.items():
            if set(column).issubset(v):
                print(idx, k)


part2()
