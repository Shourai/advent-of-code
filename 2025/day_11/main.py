with open("./testinput", "r") as file:
    input = file.read()

    dag = {}
    for line in input.splitlines():
        node, neighbours = line.split(":")
        neighbours = neighbours.strip().split()
        dag[node] = neighbours


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
