class Part1:
# Program to find most frequent
# element in a list
    def most_frequent(List):
        return max(List, key = List.count)


    with open("./input","r") as f:
        data = f.read()
        data = data.splitlines()

    length = data[0].__len__()

    array = []

    for idx, _ in enumerate(data[0]):
        arr = []
        for el in data:
            arr.append(el[idx])
        array.append(arr)

    binary = ""

    for i in array:
        binary += most_frequent(i)

    bin_a = int(binary,base=2)
    bin_b = 2**length - 1 - bin_a

    print(bin_a * bin_b)


class Part2:
# Program to find most frequent
# element in a list
    def most_frequent(self, List):
        return max(List, key=List.count)


    def least_frequent(self, List):
        return min(List, key=List.count)


    def getData(self):
        with open("./input", "r") as f:
            data = f.read()
            data = data.splitlines()
        return data


    def getMostFrequent(self,info, index):
        if len(info) == 2:
            return str(1)
        return self.most_frequent([i[index] for i in info])


    def getLeastFrequent(self,info, index):
        if len(info) == 2:
            return str(0)
        return self.least_frequent([i[index] for i in info])


    gasArray = []


    def gasRating(self, kind, info, index=0):
        array = []
        if kind == "oxygen":
            mostFreq = self.getMostFrequent(info, index)
        elif kind == "carbon":
            mostFreq = self.getLeastFrequent(info, index)

        for i in info:
            if i[index] == mostFreq:
                array.append(i)
        if len(array) == 1:
            self.gasArray.append(int(array[0], base=2))
            return
        index += 1
        self.gasRating(kind, array, index)


    def run(self):
        data = self.getData()
        self.gasRating("oxygen", data)
        self.gasRating("carbon", data)
        print(self.gasArray[0] * self.gasArray[1])

Part1()
Part2().run()
