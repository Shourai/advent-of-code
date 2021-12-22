class Part1:
    def readInput(self):
        with open("./testinput", "r") as fd:
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
        brackets = { "{": "}", "(":")", "[":"]", "<":">" }

        stack = []
        data = self.readInput()
        test = data[1]
        for idx, ch  in enumerate(test):
            if ch in brackets.values():
                if brackets[stack[idx-1]] == ch and idx != 0 :
                    stack.pop()
            else:
                stack.append(ch)
        print(stack)









Part1().findCorrupted()
