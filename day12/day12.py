class Part1:

    graph = {"start": ["A", "b"],
             "A": ["c", "b"],
             "b": ["d", "end"],
             "c": ["A"],
             "d": ["b"],
             "end": ["A", "b"]}

    n = len(graph)  # number of nodes in graph
    visited = {"start": False,
               "A": False,
               "b": False,
               "c": False,
               "d": False,
               "end": False}

    def readInput(self):
        with open("./day12/testinput", "r") as fd:
            data = fd.read()
            data = data.splitlines()
            print(data)

    def dfs(self, node):
        if self.visited[node]:
            return
        print(node)
        self.visited[node] = True

        neighbours = self.graph[node]
        for next in neighbours:
            self.dfs(next)

    def run(self):
        self.dfs("start")


Part1().run()
