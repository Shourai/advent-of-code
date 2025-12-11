with open("./input", "r") as file:
    text = file.read()
    dag = {}
    for line in text.strip().splitlines():
        node, neighbors = line.split(":")
        node = node.strip()
        neighbors = neighbors.strip().split()  # split on spaces
        dag[node] = neighbors


def count_paths(graph, start, goal):
    count = [0]

    def dfs(node):
        if node == goal:
            count[0] += 1
            return
        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(start)
    return count[0]


print(count_paths(dag, "you", "out"))
