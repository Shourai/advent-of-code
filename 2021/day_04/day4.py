import numpy as np


class Part1:

    def __init__(self):
        pass

    def readInput(self):
        with open("./day4/input", "r") as f:
            data = f.read()
            data = data.splitlines()
        bingoList = data[0].split(",")
        boards = list(filter(None, data[2::]))
        convertToArrays = [i.split() for i in boards]
        allBingoBoards = np.array_split(convertToArrays, len(boards) / 5)
        matrixOfBingoBoards = [np.array(board, ndmin=2) for board in allBingoBoards]
        return bingoList, matrixOfBingoBoards

    def crossOffBingo(self):
        bingoList, bingoMatrix = self.readInput()
        for i in bingoList:
            for board in bingoMatrix:
                board[np.where(board == i)] = "X"
                if self.checkBingo(board) == "Bingo":
                    self.calculateScore(board, i)
                    return

    def checkBingo(self, board):
        for i in range(5):
            if len(set(board[:, i])) == 1 or len(set(board[i, :])) == 1:
                return "Bingo"

    def calculateScore(self, board, num):
        unmarkedNumbers = [int(i) for i in np.nditer(board) if i != "X"]
        print(sum(unmarkedNumbers) * int(num))

    def play(self):
        self.crossOffBingo()


class Part2:

    def __init__(self):
        pass

    def readInput(self):
        with open("./day4/input", "r") as f:
            data = f.read()
            data = data.splitlines()
        bingoList = data[0].split(",")
        boards = list(filter(None, data[2::]))
        convertToArrays = [i.split() for i in boards]
        allBingoBoards = np.array_split(convertToArrays, len(boards) / 5)
        matrixOfBingoBoards = [np.array(board, ndmin=2) for board in allBingoBoards]
        return bingoList, matrixOfBingoBoards

    def crossOffBingo(self):
        bingoList, bingoMatrix = self.readInput()
        stepsTillBingo = []
        for board in bingoMatrix:
            for idx, num in enumerate(bingoList):
                board[np.where(board == num)] = "X"
                if self.checkBingo(board) == "Bingo":
                    stepsTillBingo.append((idx, num, board))
                    break
            continue

        LastWinningBoard = max(stepsTillBingo)
        self.unmarkedNumbers(LastWinningBoard[2], LastWinningBoard[1])

    def checkBingo(self, board):
        for i in range(5):
            if len(set(board[:, i])) == 1 or len(set(board[i, :])) == 1:
                return "Bingo"

    def unmarkedNumbers(self, board, num):
        numbers = [int(i) for i in np.nditer(board) if i != "X"]
        print(sum(numbers) * int(num))

    def play(self):
        self.crossOffBingo()


Part1().play()
Part2().play()
