from collections import deque

with open('day9-input') as file:
    data = file.read().split()
    data = [int(i) for i in data]

preambleLength = 25
preamble = deque(data[0:preambleLength])
numberList = data[preambleLength:]
numberList2 = []


for num in numberList:
    for idx1 in range(len(preamble)):
        for idx2 in range(len(preamble)):
            if preamble[idx1] + preamble[idx2] == num and preamble[-1] != num:
                preamble.popleft()
                preamble.append(num)
                numberList2.append(num)
                # print(preamble)

    # preamble = findNumber(num, preamble)
    # print(preamble)

for i in range(len(numberList2)):
    if numberList2[i] != numberList[i]:
        endidx = i
        invalidNumber = numberList[i]
        print(invalidNumber)
        break

numberListPart2 = numberList[0:endidx]

for i in range(len(numberListPart2)):
    for j in range(0, len(numberListPart2)):
        # print(numberListPart2[i:j])
        if sum(numberListPart2[i:j]) == invalidNumber:
            # print(numberListPart2[i:j])
            # print(sum(numberListPart2[i:j]))
            # print(invalidNumber)
            # print(numberList2[i:j])

            x = sorted(numberListPart2[i:j])
            print(x[0] + x[-1])
