data = open(0).read().strip().split(",")


def main():
    factor = 17
    modulo = 256

    # hashmap will be a dictionary of dictionaries. Dictionaries are insertion ordered as of Python 3.6
    hashmap = {}  # { 0: {rn: 1, cm: 2}, 3: {...} }

    for seq in data:
        label = ""
        focal_length = ""
        remove = False

        if "=" in seq:
            label, focal_length = seq.split("=")
        if "-" in seq:
            label, _ = seq.split("-")
            remove = True

        current_value = 0
        for ch in label:
            current_value += ord(ch)
            current_value *= factor
            current_value %= modulo

        # print(label, current_value, focal_length)

        # Remove box
        if remove and hashmap.get(current_value) is not None:
            if hashmap[current_value].get(label) is not None:
                hashmap[current_value].pop(label)
            continue

        # Add or update box
        if hashmap.get(current_value) is not None:
            hashmap[current_value].update({label: focal_length})
        else:
            hashmap[current_value] = {label: focal_length}

    # print(hashmap)

    sum = 0
    for box, v in hashmap.items():
        for slot, foc_len in enumerate(v.items()):
            sum += (int(box) + 1) * (slot + 1) * int(foc_len[1])
    print(sum)


if __name__ == "__main__":
    main()
