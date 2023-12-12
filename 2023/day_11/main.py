grid = open(0).read().splitlines()

def main(expansion: int):
# Find columns and rows without galaxies
    row_without_galaxies = []
    col_without_galaxies = []

    for row_idx, row in enumerate(grid):
        if "#" not in row:
            row_without_galaxies.append(row_idx)

## Transpose matrix to easily iterate through columns
    for col_idx, col in enumerate(zip(*grid)):
        if "#" not in col:
            col_without_galaxies.append(col_idx)



# Get coordinates of all galaxies
    galaxies = []

    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if col == "#":
                galaxies.append((row_idx, col_idx))

    galaxies = sorted(galaxies)

# Expand galaxies
    expanded_galaxies = []
    for galaxy in galaxies:
        temp_galaxy_row = galaxy[0]
        temp_galaxy_col = galaxy[1]
        for r in row_without_galaxies:
            if galaxy[0] > r:
                temp_galaxy_row += (expansion - 1)
        for c in col_without_galaxies:
            if galaxy[1] > c:
                temp_galaxy_col += (expansion - 1)
        expanded_galaxies.append((temp_galaxy_row, temp_galaxy_col))


    galaxies = expanded_galaxies

# Distances between galaxies in (x, y) by taking the differences
    paths = []
    for idx, i in enumerate(galaxies):
        for j in galaxies[idx+1::]:
            paths.append(tuple(map(lambda x,y: y - x, i, j )))

# Total distance between galaxies is x + y
    sum = 0
    for i in paths:
        sum += abs(i[0]) + abs(i[1])

    print(sum)

if __name__ == "__main__":
    main(1)
    main(1000000)
