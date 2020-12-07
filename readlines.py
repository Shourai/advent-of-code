with open('test-input') as file:
    # newLines = [x.strip().split() for x in file.read().split('\n\n')]
    data = [list(map(set, line.splitlines()))
            for line in file.read().split('\n\n')]

print(data)
