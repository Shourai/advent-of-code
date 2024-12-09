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
    right = len(blocks) - 1
    left = 0

    print(blocks)
    while left < right:
        if blocks[left] == "." and right >= 0:
            blocks[left] = blocks[right]
            blocks[right] = "x"  # Mark as processed
            right -= 1

            # Move the right pointer to the left as long as there is a dot
            while blocks[right] == "." and right >= 0:
                blocks[right] = "x"
                right -= 1
        left += 1

    print(blocks)
    return blocks


def file_compacting_p2(blocks):
    """
    Use two 'dynamic' sliding windows, one from the left and one from the right
    """
    print(blocks)

    l1 = l2 = 0
    r1 = r2 = -1

    left_window = []
    right_window = []
    # Merged sliding window logic from both sides
    i = 0
    j = len(blocks) - 1

    while i <= j:
        # Left sliding window (searching for gaps ".")
        if blocks[i] == ".":
            l1 = i
            while i <= j and blocks[i] == ".":
                i += 1
            l2 = i
            left_window.append(blocks[l1:l2])
            print(
                "Left Window:", l1, l2, blocks[l1:l2]
            )  # Prints the left window with gaps

        # Right sliding window (searching for same digits)
        if blocks[j] != "." and (i <= j):  # Make sure i <= j before proceeding
            r1 = j + 1  # Add 1 to adjust for the slicing location
            while j >= i and blocks[j] != "." and blocks[j] == blocks[j - 1]:
                j -= 1
            r2 = j
            right_window.append(blocks[r2:r1])
            print(
                "Right Window:", r1, r2, blocks[r2:r1]
            )  # Prints the right window with repeated digits

        # Move towards the center
        i += 1
        j -= 1

    for i, j in zip(left_window, right_window):
        print(i, j)


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
