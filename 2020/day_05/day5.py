largest = 0
seatIDs = []

with open('day5-input') as file:
    lines = file.read().splitlines()

    for seat in lines:
        rows = [i for i in range(128)]
        for row in range(0, 8):
            if seat[row] == "B":
                rows = rows[len(rows)//2:]
            elif seat[row] == "F":
                rows = rows[:len(rows)//2]
        columns = [i for i in range(8)]
        for column in range(7, 10):
            if seat[column] == "L":
                columns = columns[:len(columns)//2]
            if seat[column] == "R":
                columns = columns[len(columns)//2:]
        seatid = int(columns[0]) + int(rows[0]) * 8
        # if not (int(columns[0]) == 0 or int(columns[0]) == 127):
        seatIDs.append(seatid)


IDs = set(sorted(seatIDs))

a = {i for i in range(45, 954)}

print(a.difference(IDs))
