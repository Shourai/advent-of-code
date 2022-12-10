import re

# Create stacks
stacks: dict[str, list] = dict()

# create list of moves
moves: list[list[int]] = list()


def readInput():
    with open("./input", "r") as input:
        numberOfStacks: int = 0
        for line in input:
            if "1" in line:
                numberOfStacks = len(list(map(int, re.findall(r"\d+", line))))
                createStack(numberOfStacks)
                break
    with open("./input", "r") as input:
        for line in input:
            if "[" in line:
                populateStacks(line)
            elif "move" in line:
                moves.append(list(map(int, re.findall(r"\d+", line))))


def createStack(numberOfStacks):
    for i in range(1, numberOfStacks+1):
        stacks["stack_"+str(i)] = list()


def populateStacks(line):
    count = 1
    for i in range(1, len(line), 4):
        if line.strip('\n')[i] == "1":
            print(line.strip('\n')[i])
        char = line.strip('\n')[i]
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
    print(stacks)

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
