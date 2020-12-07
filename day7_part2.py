import re

AoCInput = "day7-input"

bagList = {}

shinyGoldBags = ""

with open(AoCInput) as file:
    lines = file.readlines()
    for line in lines:
        if re.search('shiny gold bags contain', line):
            shinyGoldBags = line


goldBagContains = re.findall(r'(\d*) (\w* \w*) bag[s]?', shinyGoldBags)
print(goldBagContains)


generalTree = list()


def nextLayer(prevLayer):
    layer = []
    layer.append(prevLayer)
    for color in prevLayer:
        with open(AoCInput) as file:
            lines = file.readlines()
            for line in lines:
                if re.findall(f'{color[1]} bags contain', line):
                    bagContains = re.findall(r'(\d*) (\w* \w*) bag[s]?', line)
                    generalTree.append(bagContains)
                    print(bagContains)
    return layer


generalTree.append(nextLayer(goldBagContains))
print(generalTree)
