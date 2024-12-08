from itertools import product
from pprint import pprint

with open("./testinput", "r") as f:
    grid = []
    for line in f:
        grid.append(list(line.split()[0]))


def get_nodes():
    pprint(grid)
    # Record coordinates of nodes into dictionarrow:
    node_coordinates = {}

    for row in range(len(grid[0])):
        for col in range(len(grid[row])):
            node = grid[row][col]
            node_coordinate = (row, col)
            if node != "." and node != "#":
                if node in node_coordinates:
                    node_coordinates[node].append(node_coordinate)
                else:
                    node_coordinates[node] = [node_coordinate]
    print(node_coordinates)
    return node_coordinates


def get_antinode_coordinates_p1(node_coordinates: dict):
    antinode_coordinates = []

    for node, coordinates in node_coordinates.items():
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                diff = tuple(map(lambda x, y: x - y, coordinates[i], coordinates[j]))
                a = tuple(map(lambda x, y: x + y, coordinates[i], diff))
                b = tuple(map(lambda x, y: x - y, coordinates[j], diff))
                print("Antinodes: ", a, b)
                if 0 <= a[0] < len(grid) and 0 <= a[1] < len(grid[0]):
                    antinode_coordinates.append(a)
                if 0 <= b[0] < len(grid) and 0 <= b[1] < len(grid[0]):
                    antinode_coordinates.append(b)
    print(len(set(antinode_coordinates)))

def get_antinode_coordinates_p2(node_coordinates: dict):
    antinode_coordinates = []

    for node, coordinates in node_coordinates.items():
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                diff = tuple(map(lambda x, y: x - y, coordinates[i], coordinates[j]))
                a = tuple(map(lambda x, y: x + y, coordinates[i], diff))
                b = tuple(map(lambda x, y: x - y, coordinates[j], diff))
                print("Antinodes: ", a, b)
                if 0 <= a[0] < len(grid) and 0 <= a[1] < len(grid[0]):
                    antinode_coordinates.append(a)
                if 0 <= b[0] < len(grid) and 0 <= b[1] < len(grid[0]):
                    antinode_coordinates.append(b)
    print(len(set(antinode_coordinates)))

if __name__ == "__main__":
    node_coordinates = get_nodes()
    get_antinode_coordinates_p1(node_coordinates)
    get_antinode_coordinates_p2(node_coordinates)
