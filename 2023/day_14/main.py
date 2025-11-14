from collections import defaultdict
from typing import Literal

type GridElement = Literal[".", "O", "#"]


cube_rows: dict[int, list[int]] = defaultdict(lambda: [])
cube_cols: dict[int, list[int]] = defaultdict(lambda: [])
round_stones: list[bool]

with open("./input-bastian.txt") as fh:
    grid: list[list[GridElement]] = [[*line.strip()] for line in fh if line.strip()]  # pyright: ignore[reportAssignmentType]

    num_rows = len(grid)
    num_cols = len(grid[0])

    round_stones = [False] * num_rows * num_cols

    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            match col:
                case "#":
                    cube_rows[row_idx].append(col_idx)
                    cube_cols[col_idx].append(row_idx)
                case "O":
                    round_stones[col_idx + row_idx * num_cols] = True
                case _:
                    pass


def get_row(idx) -> list[int]:
    global round_stones, num_rows, num_cols
    start_index = idx * num_cols
    end_index = start_index + num_cols
    row = round_stones[start_index:end_index]
    return [pos for pos, value in enumerate(row) if value]


def set_row(idx, arr: list[bool]) -> None:
    global round_stones, num_rows, num_cols
    start_index = idx * num_cols
    end_index = start_index + num_cols
    round_stones[start_index:end_index] = arr


def get_col(idx) -> list[int]:
    global round_stones, num_rows, num_cols
    start_index = idx
    end_index = num_rows * num_cols - (num_cols - idx) + 1
    col = round_stones[start_index:end_index:num_cols]
    return [pos for pos, value in enumerate(col) if value]


def set_col(idx, arr: list[bool]) -> None:
    global round_stones, num_rows, num_cols
    start_index = idx
    end_index = num_rows * num_cols - (num_cols - idx) + 1
    round_stones[start_index:end_index:num_cols] = arr


cache: list[tuple[list[bool], list[bool]]] = []

for j in range(1000):
    input = round_stones[:]

    found = False

    for cache_idx, (key, value) in enumerate(cache):
        if key == round_stones:
            print(f"{j}: Used: {cache_idx}")
            loop_size = j + 1 - cache_idx
            print(len(cache))

            final_idx = ((1000000000 - cache_idx) % loop_size) + cache_idx
            print(final_idx)
            sum = 0
            for x in range(num_rows):
                for y in range(num_cols):
                    if cache[final_idx][1][y + x * num_cols]:
                        sum += num_rows - x
            print(sum)
            exit()

    if found:
        continue

    for col_idx in range(0, num_cols):
        cur_idx = 0
        cube_pointer = 0
        output = [False] * num_rows

        round_stones_col = get_col(col_idx)
        cube_stones_col = cube_cols[col_idx]

        i = 0
        while i < len(round_stones_col):
            if (
                cube_pointer >= len(cube_stones_col)
                or round_stones_col[i] < cube_stones_col[cube_pointer]
            ):
                output[cur_idx] = True
                cur_idx += 1
                i += 1
            else:
                cur_idx = cube_stones_col[cube_pointer] + 1
                cube_pointer += 1

        set_col(col_idx, output)

    for row_idx in range(0, num_rows):
        cur_idx = 0
        cube_pointer = 0
        output = [False] * num_rows

        round_stones_row = get_row(row_idx)
        cube_stones_row = cube_rows[row_idx]

        i = 0
        while i < len(round_stones_row):
            if (
                cube_pointer >= len(cube_stones_row)
                or round_stones_row[i] < cube_stones_row[cube_pointer]
            ):
                output[cur_idx] = True
                cur_idx += 1
                i += 1
            else:
                cur_idx = cube_stones_row[cube_pointer] + 1
                cube_pointer += 1

        set_row(row_idx, output)

    for col_idx in range(0, num_cols):
        cur_idx = num_rows - 1
        cube_pointer = 0
        output = [False] * num_rows

        round_stones_col = get_col(col_idx)
        cube_stones_col = cube_cols[col_idx][::-1]

        i = len(round_stones_col) - 1
        while i >= 0:
            if (
                cube_pointer >= len(cube_stones_col)
                or round_stones_col[i] > cube_stones_col[cube_pointer]
            ):
                output[cur_idx] = True
                cur_idx -= 1
                i -= 1
            else:
                cur_idx = cube_stones_col[cube_pointer] - 1
                cube_pointer += 1

        set_col(col_idx, output)

    for row_idx in range(0, num_rows):
        cur_idx = num_rows - 1
        cube_pointer = 0
        output = [False] * num_rows

        round_stones_row = get_row(row_idx)
        cube_stones_row = cube_rows[row_idx][::-1]

        i = len(round_stones_row) - 1
        while i >= 0:
            if (
                cube_pointer >= len(cube_stones_row)
                or round_stones_row[i] > cube_stones_row[cube_pointer]
            ):
                output[cur_idx] = True
                cur_idx -= 1
                i -= 1
            else:
                cur_idx = cube_stones_row[cube_pointer] - 1
                cube_pointer += 1

        set_row(row_idx, output)

    cache.append((input, round_stones[:]))
