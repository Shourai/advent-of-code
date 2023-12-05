import numpy as np


# amount of segments
# zero: 6
# one: 2
# two: 5
# three: 5
# four: 4
# five: 5
# six: 6
# seven: 3
# eight: 7
# nine: 6


class Part1:
    def readInput(self):
        with open("./day8/input", "r") as fd:
            data = fd.read()
            data = data.splitlines()
            data = [i.split("|")[1].split() for i in data]

            count = 0

            for digitList in data:
                for digit in digitList:
                    if len(digit) in [2, 4, 3, 7]:
                        count += 1

            print(count)

#   6      3    7   1    8      5      0     2     9      4       9    7      8    1
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# Find eight
# Find one, four, seven -> they contain "cbgfe"
# Nine must be 6 characters long and contain "cdbgf" (7+4)-> "gfcbed"
# 6 characters long which doesn't contain "gc" (1) must be 6 -> "edbfga"
# Zero must be remaining 6 character long -> "acbgfd"
# Three, 5 characters long and contains "gc" (1) -> "begcd"
# Five, 5 characters long and adding "gc" (1) must gives Nine -> "fbgde"
# Two, 5 characters, remaining -> "abcde"


class Part2:
    def readInput(self):
        with open("./day8/testinput", "r") as fd:
            data = fd.read()
            data = data.splitlines()
            data = [i.split("|") for i in data]

            fourDigitValueList = []
            for test in data:
                inputValues = list(map(set, test[0].split()))
                outputValues = list(map(set, test[1].split()))

                values = {i: "" for i in range(10)}

                # Check off 1,4,7,8
                for i in inputValues:
                    if len(i) == 2:
                        values[1] = i
                    elif len(i) == 4:
                        values[4] = i
                    elif len(i) == 3:
                        values[7] = i
                    elif len(i) == 7:
                        values[8] = i

                for i in inputValues:
                    if len(i) == 6:
                        # Find Nine
                        if values[4].issubset(i):
                            values[9] = i
                    # Find zero
                        elif values[1].issubset(i):
                            values[0] = i
                    # Find six
                        else:
                            values[6] = i

                for i in inputValues:
                    # Find five
                    if len(i) == 5:
                        if i.issubset(values[6]):
                            values[5] = i
                    # Find three
                        elif values[1].issubset(i):
                            values[3] = i
                    # Find two
                        else:
                            values[2] = i

                digitValues = ""

                for i in outputValues:
                    for k, v in values.items():
                        if i == v:
                            digitValues += str(k)

                fourDigitValueList.append(int(digitValues))

            print(fourDigitValueList)
            print(sum(fourDigitValueList))


Part2().readInput()
