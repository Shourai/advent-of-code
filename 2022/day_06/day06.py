# Test cases
testCases = ["bvwbjplbgvbhsrlpgdmjqwftvncz", "nppdvjthqldpwncqszvftbrmjlhg",
             "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]


def markers(DistinctCharacters):
    for test in testCases:
        for i in range(DistinctCharacters, len(test)):
            if len(set(test[i-DistinctCharacters:i])) == DistinctCharacters:
                print(i)
                break

# Actual input
    with open("./input", "r") as input:
        input = input.read()
        for i in range(DistinctCharacters, len(input)):
            if len(set(input[i-DistinctCharacters:i])) == DistinctCharacters:
                print(i)
                break


# part 1
print("Part 1:")
markers(4)
# part 2
print("Part 2:")
markers(14)
