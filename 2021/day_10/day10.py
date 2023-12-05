class Part1:
    def readInput(self):
        with open("./input", "r") as fd:
            data = fd.read()
            data = data.splitlines()
            # print(data)
            data = list(map(list, data))
            return data

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


class Part2:
    def readInput(self):
        with open("./input", "r") as fd:
            data = fd.read()
            data = data.splitlines()
            # print(data)
            data = list(map(list, data))
            return data

    def findIncomplete(self):
        brackets = {"{": "}", "(": ")", "[": "]", "<": ">"}
        points = {")": 1, "]": 2, "}": 3, ">": 4}

        data = self.readInput()
        totalStack = []
        for line in data:
            stack = []
            for ch in line:
                if ch in brackets:
                    stack.append(ch)
                elif ch in brackets.values() and brackets[stack[-1]] == ch:
                    stack.pop()
                else:
                    stack = []
                    break
            if stack:
                tmp = list(map(lambda x: brackets[x], stack))
                tmp.reverse()
                totalStack.append(tmp)

        pointList = []
        for stack in totalStack:
            totalPoints = 0
            for ch in stack:
                totalPoints *= 5
                totalPoints += points[ch]
            pointList.append(totalPoints)

        # Find middle index
        middle_idx = len(pointList) // 2
        print(sorted(pointList)[middle_idx])


Part2().findIncomplete()
