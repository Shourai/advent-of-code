from collections import deque
from pprint import pprint


with open("./input") as f:
    maze_xy = [tuple(map(int,(i.strip().split(',')))) for i in f.readlines()]

rows, columns = 70,70
start = (0, 0)  # Starting position (row, column)
end = (rows, columns)  # Ending position (row, column)

def create_maze(maze_xy):
    maze = []

    for _ in range(rows+1):
        maze.append(['.'] * (columns+1))
    bytes_counter = 0
    for row,col in maze_xy:
        maze[col][row] = '#'
        bytes_counter += 1
        if shortest_path_in_maze(maze, start, end) == -1:
            print(row,col)
            break

    # return maze

def shortest_path_in_maze(maze, start, destination):
    # Directions to move in the maze: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(maze), len(maze[0])

    # Initialize the queue with the start position and the initial distance
    queue = deque([(start, 0)])
    visited = set(start)

    # Perform BFS
    while queue:
        (x, y), dist = queue.popleft()

        # Check if we've reached the destination
        if (x, y) == destination:
            return dist

        # Explore all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the new position is within bounds and is an open path
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))

    # If there's no path from start to destination
    return -1


if __name__ == "__main__":
    create_maze(maze_xy)
    # print(shortest_path_in_maze(maze, start,end))
