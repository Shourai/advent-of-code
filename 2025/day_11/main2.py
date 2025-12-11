with open("./input", "r") as file:
    text = file.read()
    dag = {}
    for line in text.strip().splitlines():
        node, neighbors = line.split(":")
        node = node.strip()
        neighbors = neighbors.strip().split()  # split on spaces
        dag[node] = neighbors


from functools import lru_cache


def count_paths(graph, start, goal):
    @lru_cache(None)
    def dfs(node, seen_dac, seen_fft):
        # Goal reached → return 1 only if both required nodes were visited
        if node == goal:
            return int(seen_dac and seen_fft)

        total = 0
        for neighbor in graph[node]:
            total += dfs(
                neighbor,
                seen_dac or (neighbor == "dac"),
                seen_fft or (neighbor == "fft"),
            )
        return total

    # Start DFS: mark whether start itself is dac/fft
    return dfs(start, start == "dac", start == "fft")


print(count_paths(dag, "svr", "out"))
