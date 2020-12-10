import re
import pprint as pp

AoCInput = "test-input"

bagList = {}

with open(AoCInput) as file:
    lines = file.readlines()
    for line in lines:
        if re.search(r'no other bags', line):
            m = line.split()
            bagList[m[0] + ' ' + m[1]] = {}
        else:
            outside = re.search(r'(\w* \w*)', line)
            inside = re.findall(r'(\d)+ (\w* \w*)', line)
            bagList[outside.group()] = {i[1]: int(i[0]) for i in inside}


def countBags(bagList, currentBag):
    count = 1
    for bag in bagList[currentBag]:
        qty = bagList[currentBag][bag]
        count += qty * countBags(bagList, bag)
    return count


print(countBags(bagList, 'shiny gold') - 1)

# print(countBags('shiny gold', colorList) - 1)
