data = open(0).read().splitlines()


def part2():
    to_predict = []

    for line in data:
        to_predict.append([int(i) for i in line.split()])

    sum = 0
    for seq in to_predict:
        sequences = []
        sequences.append(seq)
        create_next_sequence(seq, sequences)
        # print(sequences)
        new_seq = fill_placeholders(sequences)
        sum += new_seq[-1][0]
    print(sum)

def create_next_sequence(seq, sequences):
    if sum(seq) == 0:
        return
    else:
        next_sequence = []
        for i in range(len(seq) - 1):
            next_sequence.append(seq[i+1] - seq[i])
        sequences.append(next_sequence)
        create_next_sequence(next_sequence, sequences)

def fill_placeholders(sequences):
    new_sequence = []
    prev_seq = [0] + sequences[-1]
    new_sequence.append(prev_seq)
    for seq in sequences[-2::-1]:
        new_sequence.append([(seq[0] - prev_seq[0])] + seq)
        prev_seq = new_sequence[-1]

    return new_sequence


if __name__ == "__main__":
    part2()
