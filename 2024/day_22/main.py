from collections import Counter
from functools import reduce

with open("./input") as f:
    secret = f.readlines()
    secret = [int(i.strip()) for i in secret]

# print(secret)


def main(secret):
    # Multiply by 64 or bitshift left by 6
    result = secret << 6

    # mix results (bitwise XOR)
    secret = result ^ secret

    # Prune (modulo 16777216)
    secret = secret % 16777216

    # Floor divide by 32  bitshift right by 5
    result = secret >> 5

    # mix results (bitwise XOR)
    secret = result ^ secret

    # Prune (modulo 16777216)
    secret = secret % 16777216

    # Multiply by 2048 or bitshift left by 11
    result = secret << 11

    # mix results (bitwise XOR)
    secret = result ^ secret

    # Prune (modulo 16777216)
    secret = secret % 16777216
    return secret


if __name__ == "__main__":
    total_sequence = {}
    for i in secret:
        changes = {}
        input = i
        change_range = []
        list_of_ones = [i % 10]
        for _ in range(2000):
            input = main(input)
            list_of_ones.append(input % 10)

        seen = set()
        for i in range(len(list_of_ones) - 4):
            a, b, c, d, e = list_of_ones[i : i + 5]
            sequence = (b - a, c - b, d - c, e - d)

            if sequence in seen:
                continue
            seen.add(sequence)

            if sequence not in total_sequence:
                total_sequence[sequence] = 0
            total_sequence[sequence] += e

    print(max(total_sequence.values()))
