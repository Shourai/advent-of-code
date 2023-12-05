def readInput():
    with open("./input", "r") as input:
        rounds = [round.replace(" ", "").strip()
                  for round in input.readlines()]
    return rounds


class Part1:
    points = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1,
              "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ": 6}

    def returnScore(self):
        totalPoints = 0
        rounds = readInput()
        for round in rounds:
            totalPoints += self.points[round]
        print(totalPoints)


class Part2:
    points = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1,
              "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}

    def returnScore(self):
        totalPoints = 0
        rounds = readInput()
        for round in rounds:
            totalPoints += self.points[round]
        print(totalPoints)


Part1().returnScore()
Part2().returnScore()
