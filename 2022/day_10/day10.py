with open("./input", "r") as input:
    input = input.read().splitlines()


class Part1:
    value: int = 1
    cycle: int = 0
    listOfSignalStrenths = list()

    def runCycle(self, cyc, val):
        for _ in range(cyc):
            self.cycle += 1
            if self.cycle == 20:
                self.listOfSignalStrenths.append(self.cycle * self.value)
            elif self.cycle == 60:
                self.listOfSignalStrenths.append(self.cycle * self.value)
            elif self.cycle == 100:
                self.listOfSignalStrenths.append(self.cycle * self.value)
            elif self.cycle == 140:
                self.listOfSignalStrenths.append(self.cycle * self.value)
            elif self.cycle == 180:
                self.listOfSignalStrenths.append(self.cycle * self.value)
            elif self.cycle == 220:
                self.listOfSignalStrenths.append(self.cycle * self.value)
        self.value += val

    def runInstructions(self):
        for instruction in input:
            if "addx" in instruction:
                self.runCycle(2, int(instruction.split()[1]))
            else:
                self.runCycle(1, 0)

        print(sum(self.listOfSignalStrenths))


# Part1().runInstructions()


class Part2:
    value: int = 1
    cycle: int = 0
    spriteList = list()
    pixelRow = str()

    def runCycle(self, cyc, val):
        for _ in range(cyc):
            if self.value + 1 == self.cycle or self.value - 1 == self.cycle or self.value == self.cycle:
                self.pixelRow += "#"
            else:
                self.pixelRow += "."

            self.cycle += 1

            if self.cycle == 40:
                self.spriteList.append(self.pixelRow)
                print(self.pixelRow)
                self.pixelRow = str()
                self.cycle = 0
        self.value += val

    def runInstructions(self):
        for instruction in input:
            if "addx" in instruction:
                self.runCycle(2, int(instruction.split()[1]))
            else:
                self.runCycle(1, 0)

        # print(self.spriteList)


Part2().runInstructions()
