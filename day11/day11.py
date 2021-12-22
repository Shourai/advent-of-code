class Part1:
    height = 0
    width = 0
    matrix = []

    def readInput(self):
        with open("./day11/testinput", "r") as fd:
            data = fd.read()
            data = data.splitlines()
            matrix = [list(map(int, i)) for i in data]  # Create matrix with every line being one item in y-direction
            self.height = len(matrix)
            self.width = len(matrix[0])
            matrix = list(map(list, zip(*matrix)))  # Transpose the matrix
        self.matrix = matrix

    def stepIncrease(self):
        # neighbours = [(x-1), (x+1), (y-1), (y+1), (x-1, y+1), (x-1, y-1), (x+1, y+1), (x+1, y-1)]

        for x in range(self.width):
            for y in range(self.height):
                if self.matrix[x][y] > 9:
                    self.matrix[x][y] = 0
                    self.checkFlash()
                else:
                    self.matrix[x][y] += 1

    def checkFlash(self):
        print(self.matrix)

    def run(self):
        self.readInput()
        self.stepIncrease()
        self.checkFlash()


Part1().run()
