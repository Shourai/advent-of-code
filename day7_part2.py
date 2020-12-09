import re

AoCInput = "test-input"

colorList = []

with open(AoCInput) as file:
    lines = file.readlines()
    for line in lines:
        if re.search(r'no other bags', line):
            m = line.split()
            colorList.append({m[0] + ' ' + m[1]: None})
        else:
            outside = re.search(r'(\w* \w*)', line)
            inside = re.findall(r'(\d)+ (\w* \w*)', line)
            colorList.append(
                {outside.group(): {i[1]: int(i[0]) for i in inside}})

# print(colorList)


def findColor(color):
    for i in colorList:
        if list(i.keys())[0] == color:
            color2 = i
            print(color2)

    for i in color2.values():
        if i is None:
            continue
        for j in i.keys():
            findColor(j)


# Find shiny gold bag
for color in colorList:
    if list(color.keys())[0] == "shiny gold":
        shinyGold = color

for i in shinyGold.values():
    for j in i.keys():
        findColor(j)

# find color in list
