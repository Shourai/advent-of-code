def readInput() -> list[str]:
    with open("./input", "r") as input:
        rucksacks = [rucksack.strip() for rucksack in input.readlines()]
    return rucksacks


class Part1:
    def compareContents(self):
        rucksacks = readInput()
        prioritySum = 0
        for rucksack in rucksacks:
            firstHalf = rucksack[0:len(rucksack)//2]
            secondHalf = rucksack[len(rucksack)//2::]
            commonCharacter = "".join(
                set(firstHalf).intersection(set(secondHalf)))
            if commonCharacter.isupper():
                prioritySum += ord(commonCharacter) - 38
            else:
                prioritySum += ord(commonCharacter) - 96
        print(prioritySum)


# Part1().compareContents()


class Part2:
    def compareContents(self):
        rucksacks = readInput()
        prioritySum = 0
        groups = []
        n = 3  # chunksize
        for i in range(0, len(rucksacks), n):
            groups.append(list(map(set, rucksacks[i:i+n])))

        for group in groups:
            commonCharacter = "".join(group[0] & group[1] & group[2])
            if commonCharacter.isupper():
                prioritySum += ord(commonCharacter) - 38
            else:
                prioritySum += ord(commonCharacter) - 96
        print(prioritySum)


Part2().compareContents()
