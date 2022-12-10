import re

# Create stacks
stacks: dict[str, list] = dict()

# create list of moves
moves: list[list[int]] = list()


def readInput():
    with open("./input", "r") as input:
        input = input.read().split("\n\n")
        stackDiagram = input[0]
        moveList = input[1]
        numberOfStacks = len(stackDiagram.split("\n")[-1].split())
        createStack(numberOfStacks)

        for line in stackDiagram.split("\n")[:-1]:
            populateStacks(line)

        for line in moveList.split("\n")[:-1]:
            moves.append(list(map(int, re.findall(r"\d+", line))))


def createStack(numberOfStacks):
    for i in range(1, numberOfStacks+1):
        stacks["stack_"+str(i)] = list()


def populateStacks(line):
    count = 1
    for i in range(1, len(line), 4):
        char = line[i]
        if char.isalpha():
            stacks["stack_"+str(count)].append(char)
        count += 1


def reverseStack():
    for stack in stacks.values():
        stack.reverse()


readInput()
reverseStack()


class Part1:

    def popFromStack(self, amount, fromStack, toStack):
        for _ in range(amount):
            poppedCrate = stacks["stack_" + str(fromStack)].pop()
            stacks["stack_" + str(toStack)].append(poppedCrate)

    def applyMoves(self):
        for move in moves:
            self.popFromStack(move[0], move[1], move[2])

        for stack in stacks.values():
            print(stack[-1], end="")


# Part1().applyMoves()


class Part2:
    def popFromStack(self, amount, fromStack, toStack):
        poppedCrates = stacks["stack_" + str(fromStack)][-amount:]
        stacks["stack_" + str(fromStack)
               ] = stacks["stack_" + str(fromStack)][:-amount]
        stacks["stack_" + str(toStack)] = stacks["stack_" +
                                                 str(toStack)] + poppedCrates

    def applyMoves(self):
        for move in moves:
            self.popFromStack(move[0], move[1], move[2])

        for stack in stacks.values():
            print(stack[-1], end="")


Part2().applyMoves()
