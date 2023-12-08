data = open(0).read().splitlines()

# c: column
# r: row

def part1():

    # Find the symbol coordinate, with top-left being (0,0).
    num_loc = set()

    for row_idx, r in enumerate(data):
        for col_idx, c in enumerate(r):
            if c.isdigit() or c == ".":
                continue
            # Look around symbol
            for curr_row in [row_idx - 1, row_idx, row_idx + 1]:
                for curr_col in [col_idx - 1, col_idx, col_idx + 1]:
                    if curr_row < 0 or curr_row > len(data) or curr_col < 0 or curr_col > len(data[0]) or not data[curr_row][curr_col].isdigit():
                        continue
                    while curr_col > 0 and data[curr_row][curr_col - 1].isdigit():
                        curr_col -= 1
                    num_loc.add((curr_row, curr_col))
    # print(num_loc)

    total = 0
    print(len(data[0]))
    for r,c in num_loc:
        number = ""

        while c < len(data[r]) and data[r][c].isdigit():
            number += data[r][c]
            c += 1
        total += int(number)
    print(total)



def part2():
    pass


if __name__ == "__main__":
    part1()
    # part2()
