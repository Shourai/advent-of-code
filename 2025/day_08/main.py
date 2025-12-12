from pprint import pprint

with open("./input", "r") as file:
    input = [list(map(int, line.strip().split(","))) for line in file.readlines()]

connections = dict()
for i in range(len(input)):
    shortest = None
    for j in range(i + 1, len(input)):
        x_dist = input[i][0] - input[j][0]
        y_dist = input[i][1] - input[j][1]
        z_dist = input[i][2] - input[j][2]
        dSqrd = x_dist**2 + y_dist**2 + z_dist**2
        connections[dSqrd] = [input[i], input[j]]

sorted_connections = sorted(connections.items())
pprint(input)
uniques = {tuple(lst): idx for idx, lst in enumerate(input)}
pprint(uniques)

top_list = [i[1] for i in sorted_connections[:1000]]
pprint(top_list)


tuple_list = []
for i in top_list:
    x, y = i
    tuple_list.append((uniques[tuple(x)], uniques[tuple(y)]))

print(tuple_list)

# Implement union find (DSU)

parent = list(range(len(input)))


def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x


for conn in tuple_list:
    union(conn[0], conn[1])

sizes = [0] * len(parent)
for box in range(len(parent)):
    sizes[find(box)] += 1

sizes = sorted(sizes, reverse=True)
print(sizes[0] * sizes[1] * sizes[2])
