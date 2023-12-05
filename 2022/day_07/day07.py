with open("./input", "r") as input:
    input = input.read().splitlines()


stack = []
dirsize = {}

for cmd in input:
    if cmd == "$ ls" or cmd.startswith("dir"):
        continue
    if cmd.startswith("$ cd"):
        dir = cmd.split()[-1]
        if dir == "..":
            stack.pop()
        else:
            dir = f"{stack[-1]}_{dir}" if stack else dir
            stack.append(dir)
            dirsize[dir] = 0
    else:
        size, filename = cmd.split()
        for path in stack:
            dirsize[path] += int(size)

print(sum(v for v in dirsize.values() if v <= 100000))

