with open('day8-input') as file:
    newLines = file.read().strip().split('\n')
    newLines = [x.strip().split() for x in newLines]
    newLines = [[i[0], int(i[1])] for i in newLines]

haveVisited = [list() for i in range(len(newLines))]
values = [list() for i in range(len(newLines))]

index = 0
prevIndex = 0
total = 0
for i in range(len(newLines)):

    if haveVisited[index] is True:
        if newLines[i][0] == 'nop':
            newLines[i][0] = 'jmp'
        print(total)
        continue

    for j in range(len(newLines)):
        if newLines[index][0] == 'nop':
            haveVisited[index] = True
            prevIndex = index
            index += 1
        elif newLines[index][0] == 'acc':
            haveVisited[index] = True
            total += newLines[index][1]
            values[prevIndex] = total
            prevIndex = index
            index += 1
        elif newLines[index][0] == 'jmp':
            haveVisited[index] = True
            if newLines[index-1][0] == 'acc':
                prevIndex = prevIndex
                index += newLines[index][1]
            else:
                prevIndex = index
                index += newLines[index][1]


# print(haveVisited)
print(values)
# print(newLines)
