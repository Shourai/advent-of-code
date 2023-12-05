def readInput() -> list[list[str]]:
    with open("./input", "r") as input:
        sections = [section.strip() for section in input.readlines()]
        sectionPairs = [section.split(',') for section in sections]

    return sectionPairs


class Part1:
    sectionPairs = readInput()
    pairSets = []
    supersets = 0

    for s in sectionPairs:
        for j in s:
            tempSet = set()
            start, stop = list(map(int, j.split("-")))
            for i in range(start, stop + 1):
                tempSet.add(i)
            pairSets.append(tempSet)

    for i in range(0, len(pairSets), 2):
        if len(pairSets[i:i+2][0]) > len(pairSets[i:i+2][1]):
            setA: set = pairSets[i:i+2][0]
            setB: set = pairSets[i:i+2][1]
        else:
            setA: set = pairSets[i:i+2][1]
            setB: set = pairSets[i:i+2][0]

        if setA.issuperset(setB):
            supersets += 1
    print(supersets)


Part1()


class Part2:
    sectionPairs = readInput()
    pairSets = []
    intersection = 0

    for s in sectionPairs:
        for j in s:
            tempSet = set()
            start, stop = list(map(int, j.split("-")))
            for i in range(start, stop + 1):
                tempSet.add(i)
            pairSets.append(tempSet)

    for i in range(0, len(pairSets), 2):
        if len(pairSets[i:i+2][0]) > len(pairSets[i:i+2][1]):
            setA: set = pairSets[i:i+2][0]
            setB: set = pairSets[i:i+2][1]
        else:
            setA: set = pairSets[i:i+2][1]
            setB: set = pairSets[i:i+2][0]

        if setA.intersection(setB) != set():
            intersection += 1

    print(intersection)


Part2()
