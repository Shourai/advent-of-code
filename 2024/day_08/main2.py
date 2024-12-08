from itertools import product
from pprint import pprint

with open("./testinput", "r") as f:
    grid = []
    for line in f:
        grid.append(list(line.split()[0]))


def get_nodes():
    pprint(grid)
    # Record coordinates of nodes into dictionary:
    node_coordinates = {}

    for y in range(len(grid[0])):
        for x in range(len(grid[y])):
            node = grid[y][x]
            node_coordinate = (y, x)
            if node != "." and node != "#":
                if node in node_coordinates:
                    node_coordinates[node].append(node_coordinate)
                else:
                    node_coordinates[node] = [node_coordinate]
    print(node_coordinates)
    return node_coordinates


def get_antinode_coordinates(node_coordinates: dict):
    bounds_y = len(grid)
    bounds_x = len(grid[0])
    total_antinodes = []

    for node, coordinates in node_coordinates.items():
        antinodes = []
        for i in range(len(coordinates)):
            for j in range(i, len(coordinates)):
                if i != j:
                    # differences.append(tuple(map(lambda x, y: abs(x - y), coordinates[i], coordinates[j])))
                    difference1 = tuple(
                        map(lambda x, y: x - y, coordinates[i], coordinates[j])
                    )
                    difference2 = tuple(
                        map(lambda x, y: y - x, coordinates[i], coordinates[j])
                    )
                    antinodes.append(
                        tuple(map(lambda x, y: x - y, coordinates[i], difference1))
                    )
                    antinodes.append(
                        tuple(map(lambda x, y: x + y, coordinates[i], difference1))
                    )
                    antinodes.append(
                        tuple(map(lambda x, y: x - y, coordinates[j], difference1))
                    )
                    antinodes.append(
                        tuple(map(lambda x, y: x + y, coordinates[j], difference1))
                    )
                    antinodes.append(
                        tuple(map(lambda x, y: x - y, coordinates[i], difference2))
                    )
                    antinodes.append(
                        tuple(map(lambda x, y: x + y, coordinates[i], difference2))
                    )
                    antinodes.append(
                        tuple(map(lambda x, y: x - y, coordinates[j], difference2))
                    )
                    antinodes.append(
                        tuple(map(lambda x, y: x + y, coordinates[j], difference2))
                    )

        antinodes = set(antinodes).difference(node_coordinates[node])
        for y, x in antinodes:
            if y > bounds_y or y < 0 or x > bounds_x or x < 0:
                pass
            else:
                print(node, (y, x))
                total_antinodes.append((y, x))
    print(len(set(total_antinodes)))


if __name__ == "__main__":
    node_coordinates = get_nodes()
    get_antinode_coordinates(node_coordinates)
