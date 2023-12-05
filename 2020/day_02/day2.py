total = 0
with open('day2-input') as file:
    for line in file:
        output = line.strip('\n').split()
        password = output[2]
        letter = output[1][0]
        count = output[2].count(output[1][0])
        minimum = int(output[0].split('-')[0]) - 1
        maximum = int(output[0].split('-')[1]) - 1
        if (password[minimum] == letter and not password[maximum] == letter) or (password[maximum] == letter and not password[minimum] == letter):
            total += 1
        # if count >= int(minimum) and count <= int(maximum):
        #     total += 1


print(total)
