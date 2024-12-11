with open("./input") as f:
    d = f.read().split()


def main(d, blinks):
    if blinks == 25:
        # print("blinks:", blinks, d)
        print(len(d))
        return

    d2 = []
    for i in range(len(d)):
        if d[i] == "0":
            d2.append("1")
        elif len(d[i]) % 2 == 0:
            half = len(d[i]) // 2
            d2.append(d[i][:half])
            if all(j == "0" for j in d[i][half:]):
                d2.append(d[i][half : half + 1])
            else:
                d2.append(str(int(d[i][half:])))
        else:
            d2.append(str(int(d[i]) * 2024))
    blinks += 1
    main(d2, blinks)


if __name__ == "__main__":
    main(d, blinks=0)
