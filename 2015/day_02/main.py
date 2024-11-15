def part1(data):
    total = 0
    for i in data:
        l = i[0]
        w = i[1]
        h = i[2]
        sides = []
        sides.append(l * w)
        sides.append(w * h)
        sides.append(h * l)

        min_side = min(sides)
        total_surface = sum(map(lambda x: x * 2, sides))
        total += total_surface + min_side
    print(total)


if __name__ == "__main__":
    with open("./input", "r") as f:
        # input = list(map(lambda x: x.split("x"),f.read().splitlines()))
        data = f.read().splitlines()
        lst = []
        for i in data:
            lst.append(list(map(int, i.split("x"))))

    part1(lst)
