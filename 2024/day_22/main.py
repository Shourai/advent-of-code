with open("./testinput2") as f:
    secret = f.readlines()
    secret = [ int(i.strip()) for i in secret ]

print(secret)


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
    total = 0
    for i in secret:
        count = 0
        input = i
        while count < 2000:
            input = main(input)
            count += 1
        total += input
    print(total)
