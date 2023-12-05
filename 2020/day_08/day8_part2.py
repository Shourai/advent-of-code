with open('day8-input') as file:
    x = file.read().strip().split('\n')
    x = [y.split() for y in x]
    x = [[i[0], int(i[1])] for i in x]


def checkAccumulated():
    haveVisited = [False for i in range(len(x))]
    index = 0
    total = 0
    for _ in range(len(x)):
        if index < len(x):
            if haveVisited[index] is True:
                # print(total)
                # Return broken
                return(True)
            if x[index][0] == 'nop':
                haveVisited[index] = True
                index += 1
            elif x[index][0] == 'acc':
                haveVisited[index] = True
                total += x[index][1]
                index += 1
            elif x[index][0] == 'jmp':
                haveVisited[index] = True
                index += x[index][1]
    print(total)
    return(total)


def part2():
    for index in range(len(x)):
        if x[index][0] == "jmp":
            x[index][0] = "nop"
            if checkAccumulated():
                x[index][0] = "jmp"
            else:
                output = checkAccumulated()
                print(output)
        elif x[index][0] == "nop":
            x[index][0] = "jmp"
            if checkAccumulated():
                x[index][0] = "nop"
            else:
                output = checkAccumulated()
                print(output)


part2()
