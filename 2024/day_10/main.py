grid = []

with open("./input") as f:
    for line in f:
        grid.append([int(i) for i in line.strip()])


zero_coords = []
# find all coordinates of the zeroes
for y, i in enumerate(grid):
    for x, j in enumerate(i):
        if j == 0:
            zero_coords.append((x, y))


# Search around for succesive height

# boundaries
max_width = len(grid[0]) - 1
max_height = len(grid) - 1

# Search in up, down, left, right
directions = {"left": [-1, 0], "right": [1, 0], "up": [0, -1], "down": [0, 1]}


def search(x, y, valid_coordinates):
    if grid[y][x] == 9:
        valid_coordinates.add((x, y))
        # valid_coordinates.append((x, y)) # for part 2
        return

    for _, d in directions.items():
        dx, dy = d
        nx = x + dx
        ny = y + dy

        # Boundary check
        if nx < 0 or nx > max_width or ny < 0 or ny > max_height:
            continue

        if grid[ny][nx] == grid[y][x] + 1:
            search(nx, ny, valid_coordinates)


lst = []
for coord in zero_coords:
    valid_coordinates = set()
    # valid_coordinates = list() # for part 2
    x, y = coord
    search(x, y, valid_coordinates)
    lst.append(valid_coordinates)


print(sum(len(i) for i in lst))
