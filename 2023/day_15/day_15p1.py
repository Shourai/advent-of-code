data = open(0).read().strip().split(",")


def main():
    factor = 17
    modulo = 256

    sum = 0

    for seq in data:
        current_value = 0
        for ch in seq:
            current_value += ord(ch)
            current_value *= factor
            current_value %= modulo

        sum += current_value

    print(sum)


if __name__ == "__main__":
    main()
