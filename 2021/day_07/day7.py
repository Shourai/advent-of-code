import numpy as np


class Part1:
    def readInput(self):
        with open("./day7/input", "r") as fd:
            data = fd.read()
            data = data.split(",")
            data = list(map(int, data))
            data = np.array(data)
            fuelList = []
            for i in range(max(data)):
                fuelCost = np.sum(np.abs(data - i))
                fuelList.append(fuelCost)
            print(min(fuelList))


class Part2:
    def readInput(self):
        with open("./day7/input", "r") as fd:
            data = fd.read()
            data = data.split(",")
            data = list(map(int, data))
            data = np.array(data)
            horizontalMove = {}
            for i in range(max(data)):
                moves = np.abs(data - i)
                horizontalMove[i] = moves

            costs = {}
            for k, v in horizontalMove.items():
                costs[k] = self.summation(v)

            print(min(costs.values()))

    def summation(self, arr):
        newArray = []
        for i in arr:
            newArray.append(sum(range(i+1)))
        return sum(newArray)


Part2().readInput()
