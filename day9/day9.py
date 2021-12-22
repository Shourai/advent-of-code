from functools import reduce


class Part1:
    def readinput(self):
        with open("./day9/testinput", "r") as fd:
            data = fd.read()
        data = data.splitlines()

        data = list(map(list, data))

        # find length of x and y
        y_len = len(data)
        x_len = len(data[0])

        minima = []
        for y_idx, y in enumerate(data):
            for x_idx, x in enumerate(y):
                surrounding = []
                if y_idx != 0:
                    top = data[y_idx-1][x_idx]
                    surrounding.append(top)
                if y_idx != y_len - 1:
                    bottom = data[y_idx+1][x_idx]
                    surrounding.append(bottom)
                if x_idx != 0:
                    left = data[y_idx][x_idx - 1]
                    surrounding.append(left)
                if x_idx != x_len - 1:
                    right = data[y_idx][x_idx + 1]
                    surrounding.append(right)

                if x < min(surrounding):
                    minima.append(x)

        total = sum(int(i) + 1 for i in minima)
        print(total)


class Part2:
    y_len = None
    x_len = None
    setOfCoords = set()

    def readinput(self):
        with open("./day9/input", "r") as fd:
            data = fd.read()
        data = data.splitlines()

        data = list(map(list, data))
        return data

    def getMinima(self, data):
        data = data
        # find length of x and y
        self.y_len = len(data)
        self.x_len = len(data[0])
        x_len = self.x_len
        y_len = self.y_len

        # Get coordinates for minima
        minima = []
        for y_idx, y in enumerate(data):
            for x_idx, x in enumerate(y):
                surrounding = []
                if y_idx != 0:
                    top = data[y_idx-1][x_idx]
                    surrounding.append(top)
                if y_idx != y_len - 1:
                    bottom = data[y_idx+1][x_idx]
                    surrounding.append(bottom)
                if x_idx != 0:
                    left = data[y_idx][x_idx - 1]
                    surrounding.append(left)
                if x_idx != x_len - 1:
                    right = data[y_idx][x_idx + 1]
                    surrounding.append(right)

                if x < min(surrounding):
                    minima.append([y_idx, x_idx])

        return minima

    def floodFill(self, matrix, coords, count=1):
        y, x = coords

        if (y, x) in self.setOfCoords:
            return

        neighbours = [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]
        for n in neighbours:
            if 0 <= n[0] <= self.y_len - 1 and 0 <= n[1] <= self.x_len - 1 and matrix[n[0]][n[1]] != "9":
                self.setOfCoords.add((y, x))
                self.floodFill(matrix, [n[0], n[1]])

    def run(self):
        matrix = self.readinput()
        minima = self.getMinima(matrix)

        largest_basins = []

        for basin in minima:
            self.setOfCoords = set()
            self.floodFill(matrix, basin)
            largest_basins.append(len(self.setOfCoords))

        lst = sorted(largest_basins, reverse=True)[:3]
        print(reduce(lambda x, y: x*y, lst))


Part2().run()
