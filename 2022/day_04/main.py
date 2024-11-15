def solutions(data):
    counter_part1 = 0
    counter_part2 = 0

    for d in data:
        first_section = d[0].split("-")
        first_section_begin, first_section_end = list(map(int, first_section))
        second_section = d[1].split("-")
        second_section_begin, second_section_end = list(map(int, second_section))

        set_first_pair = set(range(first_section_begin, first_section_end + 1))
        set_second_pair = set(range(second_section_begin, second_section_end + 1))

        if set_first_pair.issubset(set_second_pair) or set_first_pair.issuperset(
            set_second_pair
        ):
            counter_part1 += 1

        if not set_first_pair.isdisjoint(set_second_pair):
            counter_part2 += 1
    print("Part 1: ", counter_part1)
    print("Part 2: ", counter_part2)


if __name__ == "__main__":
    with open("./input", "r") as f:
        data = f.read().splitlines()
    data = [d.split(",") for d in data]
    solutions(data)
