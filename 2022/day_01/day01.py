def readInput() -> list[list[int]]:
    with open("./input", "r") as input:
        input = input.read().split('\n\n')
        caloriesList = [list(map(int, elf.split())) for elf in input]

    return caloriesList


class Part1:
    def getHighestCalorie(self):
        caloriesList = readInput()
        print(max([sum(elf) for elf in caloriesList]))


class Part2:
    def getTopThreeCalories(self):
        caloriesList = readInput()
        caloriesPerElf = [sum(elf) for elf in caloriesList]
        print(sum(sorted(caloriesPerElf, reverse=True)[0:3]))


Part1().getHighestCalorie()
Part2().getTopThreeCalories()
