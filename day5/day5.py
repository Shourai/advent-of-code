import numpy as np


class Part1:

    lines = []

    def __init__(self):
        pass

    def readInput(self):
        with open("./day5/input", "r") as f:
            data = f.read()
            data = data.splitlines()

        coords = [i.split(" -> ") for i in data]

        self.lines = [
            {"x1": int(i[0].split(",")[0]),
             "y1": int(i[0].split(",")[1]),
             "x2": int(i[1].split(",")[0]),
             "y2": int(i[1].split(",")[1])
             } for i in coords]
        return self.lines

    def createGrid(self):
        lines = self.readInput()
        LargestXcoord = 0
        LargestYcoord = 0
        for line in lines:
            if line["x1"] > LargestXcoord:
                LargestXcoord = line["x1"]
            if line["x2"] > LargestXcoord:
                LargestXcoord = line["x2"]
            if line["y1"] > LargestYcoord:
                LargestYcoord = line["y1"]
            if line["y2"] > LargestXcoord:
                LargestYcoord = line["y2"]
        return np.zeros((LargestXcoord + 5, LargestYcoord + 5), dtype=np.int8)

    def drawLines(self):
        # Only horizontal or vertical, x1 = x2 or y1 = y2
        grid = self.createGrid()
        horizontalLines = []
        verticalLines = []
        for line in self.lines:
            if line["x1"] == line["x2"]:
                horizontalLines.append(line)
            elif line["y1"] == line["y2"]:
                verticalLines.append(line)
        for line in horizontalLines:
            if line["y1"] < line["y2"]:
                for y in range(line["y1"], line["y2"]+1):
                    x = line["x1"]
                    grid[y, x] += +1
            else:
                for y in range(line["y2"], line["y1"]+1):
                    x = line["x1"]
                    grid[y, x] += +1
        for line in verticalLines:
            if line["x1"] < line["x2"]:
                for x in range(line["x1"], line["x2"]+1):
                    y = line["y1"]
                    grid[y, x] += +1
            else:
                for x in range(line["x2"], line["x1"]+1):
                    y = line["y1"]
                    grid[y, x] += +1
        return grid

    def countOverlaps(self):
        grid = self.drawLines()
        print(len(grid[grid > 1]))


class Part2:

    lines = []

    def __init__(self):
        pass

    def readInput(self):
        with open("./day5/input", "r") as f:
            data = f.read()
            data = data.splitlines()

        coords = [i.split(" -> ") for i in data]

        self.lines = [
            {"x1": int(i[0].split(",")[0]),
             "y1": int(i[0].split(",")[1]),
             "x2": int(i[1].split(",")[0]),
             "y2": int(i[1].split(",")[1])
             } for i in coords]
        return self.lines

    def createGrid(self):
        lines = self.readInput()
        LargestXcoord = 0
        LargestYcoord = 0
        for line in lines:
            if line["x1"] > LargestXcoord:
                LargestXcoord = line["x1"]
            if line["x2"] > LargestXcoord:
                LargestXcoord = line["x2"]
            if line["y1"] > LargestYcoord:
                LargestYcoord = line["y1"]
            if line["y2"] > LargestXcoord:
                LargestYcoord = line["y2"]
        return np.zeros((LargestXcoord + 5, LargestYcoord + 5), dtype=np.int8)

    def drawLines(self):
        # Only horizontal or vertical, x1 = x2 or y1 = y2
        grid = self.createGrid()
        horizontalLines = []
        verticalLines = []
        diagonalLines = []
        for line in self.lines:
            if line["x1"] == line["x2"]:
                horizontalLines.append(line)
            elif line["y1"] == line["y2"]:
                verticalLines.append(line)
            else:
                diagonalLines.append(line)
        for line in horizontalLines:
            if line["y1"] < line["y2"]:
                for y in range(line["y1"], line["y2"]+1):
                    x = line["x1"]
                    grid[y, x] += +1
            else:
                for y in range(line["y2"], line["y1"]+1):
                    x = line["x1"]
                    grid[y, x] += +1
        for line in verticalLines:
            if line["x1"] < line["x2"]:
                for x in range(line["x1"], line["x2"]+1):
                    y = line["y1"]
                    grid[y, x] += +1
            else:
                for x in range(line["x2"], line["x1"]+1):
                    y = line["y1"]
                    grid[y, x] += +1
        for line in diagonalLines:
            x1_step = 0
            x2_step = 0
            y1_step = 0
            y2_step = 0
            x_step = 1
            y_step = 1
            if line['x1'] > line['x2']:
                x_step = -1
                x1_step = 0
                x2_step = -1
            else:
                x_step = 1
                x1_step = 0
                x2_step = 1
            if line['y1'] > line['y2']:
                y_step = -1
                y1_step = 0
                y2_step = -1
            else:
                y_step = 1
                y1_step = 0
                y2_step = 1

            # print(line)
            # print(range(line['x1'] + x1_step, line['x2'] + x2_step, x_step))
            # print(range(line['y1'] + y1_step, line['y2'] + y2_step, y_step))

            for x, y in zip(range(line['x1'] + x1_step, line['x2'] + x2_step, x_step), range(line['y1'] + y1_step, line['y2'] + y2_step, y_step)):
                # print(x, y)
                grid[y, x] += 1
        return grid

    def countOverlaps(self):
        grid = self.drawLines()
        # print(grid)
        print(len(grid[grid > 1]))


Part2().countOverlaps()
