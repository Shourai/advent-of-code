with open("./input", "r") as file:
    grid = ["." + line.strip() + "." for line in file.readlines()]
    grid = ["." * len(grid[0])] + grid + ["." * len(grid[0])]


directions = {
    "NORTH": (0, 1),
    "NORTHEAST": (1, 1),
    "EAST": (1, 0),
    "SOUTHEAST": (1, -1),
    "SOUTH": (0, -1),
    "SOUTHWEST": (-1, -1),
    "WEST": (-1, 0),
    "NORTHWEST": (-1, 1),
}


def part1():
    def check_neighbours(grid: list[str], row: int, col: int):
        rolls_of_paper_around = 0

        for drow, dcol in directions.values():
            new_row, new_col = row + drow, col + dcol

            if grid[new_row][new_col] == "@":
                rolls_of_paper_around += 1

        if rolls_of_paper_around < 4:
            return 1

        return 0

    count = 0

    for row in range(len(grid)):
        if row == 0 or row == len(grid):
            continue
        for col in range(len(grid[row])):
            if grid[row][col] == "@":
                count += check_neighbours(grid, row, col)

    print(count)


def part2():
    new_grid = [list(line) for line in grid]

    def check_neighbours(grid: list[list[str]], row: int, col: int) -> tuple:
        rolls_of_paper_around = 0

        for drow, dcol in directions.values():
            new_row, new_col = row + drow, col + dcol

            if grid[new_row][new_col] == "@":
                rolls_of_paper_around += 1

        if rolls_of_paper_around < 4:
            return (row, col)

        return (-1, -1)

    removing = True
    removed_rolls = 0
    while removing:
        removal_coordinates = []
        for row in range(len(new_grid)):
            if row == 0 or row == len(new_grid):
                continue
            for col in range(len(grid[row])):
                if new_grid[row][col] == "@":
                    if check_neighbours(new_grid, row, col) != (-1, -1):
                        removal_coordinates.append((row, col))

        if not removal_coordinates:
            removing = False
            break

        for row, col in removal_coordinates:
            new_grid[row][col] = "x"

        removed_rolls += len(removal_coordinates)

    print(removed_rolls)


part2()
