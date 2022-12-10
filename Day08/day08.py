with open("./input", "r") as input:
    input = input.read().split()


# amount of trees on outer edge
outerEdge = 2 * (len(input[0]) + len(input) - 2)


# All possible coordinates the tree can have which aren't on the edge
yCoord = len(input) - 1
xCoord = len(input[0]) - 1

allCoordinates = list()

for x in range(1, xCoord):
    for y in range(1, yCoord):
        allCoordinates.append((x, y))


# print(allCoordinates)


def getTreeHeight(x, y):
    return input[y][x]


trees = 0

for coordinate in allCoordinates:
    print("current coordinate: ", coordinate)
    currentTreeHeight = getTreeHeight(coordinate[0], coordinate[1])
    print("current tree height: ", currentTreeHeight)

    # Create list of coordinates to check
    visible = False
    left = list()
    right = list()
    top = list()
    bottom = list()

    for x in range(0, coordinate[0]):
        if getTreeHeight(x, coordinate[1]) < currentTreeHeight:
            left.append(True)
        else:
            left.append(False)

    for x in range(coordinate[0]+1, len(input[0])):
        if getTreeHeight(x, coordinate[1]) < currentTreeHeight:
            right.append(True)
        else:
            right.append(False)

    for y in range(0, coordinate[1]):
        if getTreeHeight(coordinate[0], y) < currentTreeHeight:
            top.append(True)
        else:
            top.append(False)

    for y in range(coordinate[1]+1, len(input)):
        if getTreeHeight(coordinate[0], y) < currentTreeHeight:
            bottom.append(True)
        else:
            bottom.append(False)

    print(left)
    print(right)
    print(top)
    print(bottom)

    if all(left) or all(right) or all(top) or all(bottom):
        trees += 1


print(trees + outerEdge)
