class Part1:
    def readInput(self):
        with open("./input", "r") as fd:
            data = fd.read()
            data = data.splitlines()
            # print(data)
            data = list(map(list, data))
            return data

    def findIncomplete(self):
        data = self.readInput()
        for i in data:
            if len(i) % 2 == 0:
                print(i)

    def findCorrupted(self):
        brackets = {"{": "}", "(": ")", "[": "]", "<": ">"}
        points = {")": 3, "]": 57, "}": 1197, ">": 25137}

        totalPoints = 0
        stack = []
        data = self.readInput()
        for line in data:
            for ch in line:
                if ch in brackets:
                    stack.append(ch)
                elif ch in brackets.values() and brackets[stack[-1]] == ch:
                    stack.pop()
                else:
                    totalPoints += points[ch]
                    print(ch)
                    break
        print(totalPoints)


Part1().findCorrupted()
