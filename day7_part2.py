import re
import pprint as pp

AoCInput = "test-input"

colorList = {}

with open(AoCInput) as file:
    lines = file.readlines()
    for line in lines:
        if re.search(r'no other bags', line):
            m = line.split()
            colorList[m[0] + ' ' + m[1]] = {}
        else:
            outside = re.search(r'(\w* \w*)', line)
            inside = re.findall(r'(\d)+ (\w* \w*)', line)
            colorList[outside.group()] = {i[1]: int(i[0]) for i in inside}

pp.pprint(colorList)


def countBags(color, colorList):
    count = 1
    insideBags = colorList[color]
    for i in insideBags:
        print(i)
        multiply = insideBags[i]
        count += multiply * countBags(i, colorList)
    return count


print(countBags('shiny gold', colorList) - 1)
