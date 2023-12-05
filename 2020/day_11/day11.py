from pprint import pprint
import copy

with open('day11-input') as file:
    data = file.read().split()

grid = list()
for line in data:
    grid.append(['.']+[c for c in line] + ['.'])

topAndBottom = ['.' for i in range(len(grid[1]))]
grid = [topAndBottom] + grid + [topAndBottom]

# pprint(grid)


def checkPerimiter(inputGrid):
    count = 0
    newGrid = copy.deepcopy(inputGrid)

    for y in range(1, len(inputGrid)-1):
        for x in range(1, len(inputGrid[1]) - 1):
            if inputGrid[y][x] == ".":
                continue
            if inputGrid[y-1][x-1] == "#":
                count += 1
            if inputGrid[y-1][x] == "#":
                count += 1
            if inputGrid[y-1][x+1] == "#":
                count += 1
            if inputGrid[y][x-1] == "#":
                count += 1
            if inputGrid[y][x+1] == "#":
                count += 1
            if inputGrid[y+1][x-1] == "#":
                count += 1
            if inputGrid[y+1][x] == "#":
                count += 1
            if inputGrid[y+1][x+1] == "#":
                count += 1
            if count >= 4:
                newGrid[y][x] = "L"
            elif count == 0:
                newGrid[y][x] = "#"
            count = 0

    if inputGrid == newGrid:
        return newGrid

    return checkPerimiter(newGrid)


def toggleSeat(inputGrid):
    count = 0
    newGrid = copy.deepcopy(inputGrid)
    for y in range(1, len(inputGrid)-1):
        for x in range(1, len(inputGrid[1]) - 1):
            if inputGrid[y][x] == ".":
                continue
            count += checkUDLR(inputGrid, y, x)
            count += checkDiagonal(inputGrid, y, x)
            if count >= 5:
                newGrid[y][x] = "L"
            elif count == 0:
                newGrid[y][x] = "#"
            count = 0

    if newGrid == inputGrid:
        return newGrid

    return toggleSeat(newGrid)


def checkUDLR(inputGrid, yCoord, xCoord):
    count = 0
    # Up
    for y in range(yCoord - 1, 0, -1):
        if inputGrid[y][xCoord] == "#":
            count += 1
            break
        elif inputGrid[y][xCoord] == "L":
            break
    # Down
    for y in range(yCoord + 1, len(inputGrid) - 1):
        if inputGrid[y][xCoord] == "#":
            count += 1
            break
        elif inputGrid[y][xCoord] == "L":
            break
    # Left
    for x in range(xCoord - 1, 0, -1):
        if inputGrid[yCoord][x] == "#":
            count += 1
            break
        elif inputGrid[yCoord][x] == "L":
            break
    # Right
    for x in range(xCoord + 1, len(inputGrid[1]) - 1):
        if inputGrid[yCoord][x] == "#":
            count += 1
            break
        elif inputGrid[yCoord][x] == "L":
            break
    return count


def checkDiagonal(inputGrid, yCoord, xCoord):
    count = 0
    # upper left diagonal
    for y, x in zip(range(yCoord-1, 0, -1), range(xCoord-1, 0, -1)):
        if inputGrid[y][x] == "#":
            count += 1
            break
        elif inputGrid[y][x] == "L":
            break
    # upper right diagonal
    for y, x in zip(range(yCoord-1, 0, -1), range(xCoord+1, len(inputGrid[1]) - 1, 1)):
        if inputGrid[y][x] == "#":
            count += 1
            break
        elif inputGrid[y][x] == "L":
            break
    # lower left diagonal
    for y, x in zip(range(yCoord+1, len(inputGrid)-1, 1), range(xCoord-1, 0, -1)):
        if inputGrid[y][x] == "#":
            count += 1
            break
        elif inputGrid[y][x] == "L":
            break
    # lower right diagonal
    for y, x in zip(range(yCoord+1, len(inputGrid)-1, 1), range(xCoord+1, len(inputGrid[1]) - 1, 1)):
        if inputGrid[y][x] == "#":
            count += 1
            break
        elif inputGrid[y][x] == "L":
            break

    return count


def part1():
    output = checkPerimiter(grid)
    seats = 0
    for i in output:
        for j in i:
            if j == "#":
                seats += 1
    print(seats)


def part2():
    output = toggleSeat(grid)
    seats = 0
    for i in output:
        for j in i:
            if j == "#":
                seats += 1
    print(seats)


part2()
