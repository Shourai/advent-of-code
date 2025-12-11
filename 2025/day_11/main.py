with open("./input", "r") as file:
    input = file.read()

    dag = {}
    for line in input.splitlines():
        node, neighbours = line.split(":")
        neighbours = neighbours.strip().split()
        dag[node] = neighbours


def count_paths(graph, start, goal):
    def dfs(node):
        if node == goal:
            return 1  # base case: 1 valid path
        total = 0
        for neighbor in graph[node]:
            total += dfs(neighbor)  # sum paths from each neighbor
        return total

    return dfs(start)


print(count_paths(dag, "you", "out"))
