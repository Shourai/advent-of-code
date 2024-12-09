with open("./testinput2", "r") as f:
    data = list(map(int, list(f.read().split()[0])))


def block_respresentation(data):
    """
    Create the representation of the disk map
    e.g. `12345` -> `0..111....22222`
    and return the blocks representation
    """
    blocks = []
    idx = 0
    for i, char in enumerate(data):
        if i % 2 == 0:
            blocks += char * [idx]
            idx += 1
        else:
            blocks += char * ["."]
    return blocks


def file_compacting_p1(blocks):
    """
    Use two sliding windows, one from the left and one from the right
    """
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
    return blocks


def file_compacting_p2(blocks):
    """
    Use two 'dynamic' sliding windows, one from the left and one from the right
    """
    print(blocks)

    l1 = l2 = 0
    r1 = r2 = -1

    # Dynamic sliding window from the left, looking for gaps i.e. "."
    j = 0
    while j < len(blocks):
        if blocks[j] == ".":
            l1 = j
            while blocks[j] == ".":
                j += 1
            l2 = j
            print(l1, l2, blocks[l1:l2])
        j += 1

    # Dynamic sliding window from the right, looking for same digits
    j = len(blocks) - 1
    while j > 0:
        if blocks[j] != ".":
            r1 = j + 1  # Add 1 to adjust for the slicing location
            while blocks[j] != "." and blocks[j] == blocks[j - 1]:
                j -= 1
            r2 = j
            print(r1, r2, blocks[r2:r1])
        j -= 1


def checksum(blocks):
    """
    Calculate the checksum
    """
    total = 0
    for idx, c in enumerate(blocks):
        if c != "x":
            total += idx * c

    print(total)


if __name__ == "__main__":
    blocks = block_respresentation(data)
    # blocks = file_compacting_p1(blocks)
    blocks = file_compacting_p2(blocks)
    # checksum(blocks)
