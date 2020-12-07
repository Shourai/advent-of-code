input = open("input").read().splitlines()
input = [int(i) for i in input]


for i in input:
    for j in input:
        for k in input:
            if i + j + k == 2020:
                print(i * j * k)
