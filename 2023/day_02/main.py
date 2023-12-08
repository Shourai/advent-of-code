import re


def part1():
    max_cubes = {"red": 12, "green": 13, "blue": 14}

    total = 0

    with open("./input", "r") as file:
        for line in file:
            possible_set = []
            game_id = re.findall(r"Game (\d+)", line)
            game_sets = re.findall(r"(\d+) (red|green|blue)", line)
            for game_set in game_sets:
                possible_set.append(int(game_set[0]) <= max_cubes[game_set[1]])

            if all(possible_set):
                total += int(game_id[0])
        print(total)


def part2():
    total = 0

    with open("./input", "r") as file:
        for line in file:
            cubes = {"red": 1, "green": 1, "blue": 1}
            game_sets = re.findall(r"(\d+) (red|green|blue)", line)
            for game_set in game_sets:
                if int(game_set[0]) > cubes[game_set[1]]:
                    cubes[game_set[1]] = int(game_set[0])

            total += cubes["red"] * cubes["blue"] * cubes["green"]

    print(total)


if __name__ == "__main__":
    # part1()
    part2()
