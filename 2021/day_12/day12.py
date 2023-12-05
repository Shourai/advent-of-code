from collections import defaultdict


class Part1:

    graph = defaultdict(lambda: [])
    count = 0
    path = []

    def readInput(self):
        with open("./day12/input", "r") as fd:
            data = fd.read()
            data = data.splitlines()

        for line in data:
            x, y = line.split("-")
            self.graph[x].append(y)
            self.graph[y].append(x)
        print(self.graph)

    def dfs(self, node):
        self.path.append(node)

        if node == "end":
            print(self.path)
            self.count += 1

        neighbours = self.graph[node]
        for next in neighbours:
            if next not in self.path or next.isupper():
                self.dfs(next)

        self.path.pop()

    def run(self):
        self.readInput()
        self.dfs("start")
        print(self.count)


Part1().run()
