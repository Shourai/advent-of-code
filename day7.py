import re

bagList = {}

matchList = []

with open('test-input') as file:
    lines = file.readlines()
    for line in lines:
        if re.search('no other bags', line):
            matches = re.findall(r'(\w* \w*) bags', line)
            bagList[matches[0]] = None
        else:
            matches = re.findall(r'(\w* \w*) bag[s]?', line)
            matchList.append(matches)

print(matchList)

containedBags = set()

test = set()


def initialSearch():
    for bags in matchList:
        if 'shiny gold' in bags[1:]:
            containedBags.add(bags[0])


def searchBags(containedBags):
    foundBags = set()
    for i in containedBags:
        for bags in matchList:
            if i in bags[1:]:
                foundBags.add(bags[0])
    return(foundBags)


initialSearch()

# for i in range(100):
#     output = searchBags(containedBags)
#     containedBags = containedBags.union(output)

# print(len(containedBags))

# print(matchList)
