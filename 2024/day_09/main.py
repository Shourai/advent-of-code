with open("./input", "r") as f:
    data = list(map(int, list(f.read().split()[0])))


def main():
    blocks = []
    idx = 0
    for i, char in enumerate(data):
        if i % 2 == 0:
            # print(char, idx)
            blocks += char * [idx]
            idx += 1
        else:
            # print(char, ".")
            blocks += char * ["."]

    right = -1
    for i in range(len(blocks)):
        if blocks[i] == ".":
            blocks[i] = blocks[right]
            blocks[right] = "x"
            right -= 1
            while blocks[right] == ".":
                blocks[right] = "x"
                right -= 1
        if blocks[i] == "x":
            break

    total = 0
    for idx, c in enumerate(blocks):
        if c != "x":
            total += idx * c

    print(total)


if __name__ == "__main__":
    main()
