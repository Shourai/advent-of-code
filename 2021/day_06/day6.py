class Part1:
    def readInput(self):
        with open("./day6/testinput", "r") as fd:
            data = fd.read()
            data = data.split(",")
            data = list(map(int, data))
            return data

    def newDay(self, data, day=0):
        data = list(data)
        for idx, _ in enumerate(data):
            data[idx] -= 1

            if data[idx] == -1:
                data.append(9)
                data[idx] = 6
        day += 1
        if day == 250:
            print(len(data))
            return
        self.newDay(tuple(data), day)

    def run(self):
        self.newDay(tuple(self.readInput()))


class Part2:
    def readInput(self):
        with open("./day6/input", "r") as fd:
            data = fd.read()
            data = data.split(",")
            data = list(map(int, data))
            return data

    def fishTimers(self):
        data = self.readInput()
        timers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for i in data:
            timers[i] += 1

        days = 256
        for d in range(days):
            temp = timers[0]
            for k, v in timers.items():
                if k == 6:
                    timers[k] = temp + timers[k+1]
                elif k == 8:
                    timers[8] = temp
                else:
                    timers[k] = timers[k+1]
        print(sum(timers.values()))
        print(timers)


Part2().fishTimers()
