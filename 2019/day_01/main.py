def part1():
    sum = 0

    with open("./input", "r") as file:
        for line in file:
            number = int(line.strip())
            mass = number // 3 - 2
            sum += mass
    print(sum)


def part2():

    def fuelAdder(number, sum):
        if number // 3 - 2 <= 0:
            return sum
        number = number // 3 - 2
        sum += number
        return fuelAdder(number, sum)

    total = 0

    with open("./input", "r") as file:
        for line in file:
            number = int(line.strip())
            total += fuelAdder(number, 0)
    print(total)

# Part1()

if __name__ == "__main__":
    part1()
    part2()
