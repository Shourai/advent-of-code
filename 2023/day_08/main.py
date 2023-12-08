data = open(0).readlines()


def part1():
    lines = [i.strip() for i in data]
    instructions = lines[0]
    nodes = lines[2:]
    node_dict = {}
    for node in nodes:
        n = node.split(" = ")
        node_dict[n[0]] = n[1].strip("()").split(", ")

    current_node = "AAA"
    final_node = False
    count = 0

    while not final_node:
        for i in instructions:
            if i == "R":
                current_node = node_dict[current_node][1]
                count += 1
            if i == "L":
                current_node = node_dict[current_node][0]
                count += 1
            if current_node == "ZZZ":
                final_node = True
    print(count)


def part2():
    from math import lcm
    lines = [i.strip() for i in data]
    instructions = lines[0]
    nodes = lines[2:]
    node_dict = {}
    starting_nodes = []
    for node in nodes:
        n = node.split(" = ")
        node_dict[n[0]] = n[1].strip("()").split(", ")
        if n[0][2] == "A":
            starting_nodes.append(n[0])


    l_c_m = []

    for node in starting_nodes:
        current_node = node
        count = 0
        final_node = False

        while not final_node:
            for i in instructions:
                if i == "R":
                    current_node = node_dict[current_node][1]
                    count += 1
                if i == "L":
                    current_node = node_dict[current_node][0]
                    count += 1
                if current_node[2] == "Z":
                    final_node = True
        l_c_m.append(count)

    print(lcm(*l_c_m))



if __name__ == "__main__":
    # part1()
    part2()
