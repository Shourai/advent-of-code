from pprint import pprint


class Part1:
    height = 0
    width = 0
    matrix = []
    numberOfFlashes = 0

    def readInput(self):
        with open("./day11/input", "r") as fd:
            data = fd.read()
            data = data.splitlines()
            matrix = [list(map(int, i)) for i in data]  # Create matrix with every line being one item in y-direction
            self.height = len(matrix)
            self.width = len(matrix[0])
            # matrix = list(map(list, zip(*matrix)))  # Transpose the matrix
        self.matrix = matrix

    def stepIncrease(self):

        for y in range(self.height):
            for x in range(self.width):
                self.matrix[y][x] += 1

    def checkFlash(self):
        flashedCoordinates = []
        higherThanNine = True

        while higherThanNine:
            higherThanNineCount = 0
            for y in range(self.height):
                for x in range(self.width):
                    if self.matrix[y][x] > 9:
                        higherThanNineCount += 1
                        flashedCoordinates.append((y, x))
                        self.numberOfFlashes += 1
                        neighbours = [(x-1, y), (x+1, y), (x, y-1), (x, y+1),
                                      (x-1, y+1), (x-1, y-1), (x+1, y+1), (x+1, y-1)]
                        for n in neighbours:
                            if 0 <= n[0] < self.width and 0 <= n[1] < self.height:
                                self.matrix[n[1]][n[0]] += 1
                        self.clearValue(flashedCoordinates)
            higherThanNine = higherThanNineCount > 0

    def clearValue(self, coordinates):
        for coord in coordinates:
            self.matrix[coord[0]][coord[1]] = 0

    def run(self):
        self.readInput()
        for _ in range(100):
            self.stepIncrease()
            self.checkFlash()
        print(self.numberOfFlashes)


Part1().run()


class Part2:
    height = 0
    width = 0
    matrix = []
    numberOfFlashes = 0

    def readInput(self):
        with open("./day11/input", "r") as fd:
            data = fd.read()
            data = data.splitlines()
            matrix = [list(map(int, i)) for i in data]  # Create matrix with every line being one item in y-direction
            self.height = len(matrix)
            self.width = len(matrix[0])
            # matrix = list(map(list, zip(*matrix)))  # Transpose the matrix
        self.matrix = matrix

    def stepIncrease(self):

        for y in range(self.height):
            for x in range(self.width):
                self.matrix[y][x] += 1

    def checkFlash(self):
        flashedCoordinates = []
        higherThanNine = True

        while higherThanNine:
            higherThanNineCount = 0
            for y in range(self.height):
                for x in range(self.width):
                    if self.matrix[y][x] > 9:
                        higherThanNineCount += 1
                        flashedCoordinates.append((y, x))
                        self.numberOfFlashes += 1
                        neighbours = [(x-1, y), (x+1, y), (x, y-1), (x, y+1),
                                      (x-1, y+1), (x-1, y-1), (x+1, y+1), (x+1, y-1)]
                        for n in neighbours:
                            if 0 <= n[0] < self.width and 0 <= n[1] < self.height:
                                self.matrix[n[1]][n[0]] += 1
                        self.clearValue(flashedCoordinates)
            higherThanNine = higherThanNineCount > 0

    def clearValue(self, coordinates):
        for coord in coordinates:
            self.matrix[coord[0]][coord[1]] = 0

    def checkSimulFlash(self, allZeroes, step):
        allZeroes = True
        for y in range(self.height):
            for x in range(self.width):
                if self.matrix[y][x] > 0:
                    allZeroes = False

        return allZeroes

    def run(self):
        self.readInput()
        allZeroes = False
        step = 0
        while not allZeroes:
            self.stepIncrease()
            self.checkFlash()
            allZeroes = self.checkSimulFlash(allZeroes, step)
            step += 1
        print(step)


Part2().run()
