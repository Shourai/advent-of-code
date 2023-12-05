with open('day13-input') as file:
    data = file.read().strip().split()
    departureTime = int(data[0])
    busses = [int(bus) for bus in data[1:][0].split(',') if bus != 'x']


timetable = dict()

for i in busses:
    a = [i for i in range(0, departureTime+i, i)]
    a = [i for i in a if i >= departureTime]
    timetable[i] = a


shortestWaitTime = timetable[41][0] - departureTime
for i in timetable:
    timeDiff = timetable[i][0] - departureTime
    if timeDiff < shortestWaitTime:
        shortestWaitTime = timeDiff

print(shortestWaitTime)
