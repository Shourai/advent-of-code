from copy import deepcopy

with open('day12-input') as file:
    data = file.read().split()

compass = {"E": 0, "S": 0, "W": 0, "N": 0}
directions = ["E", "S", "W", "N"]


def part1():
    currentFacingDirection = directions[0]
    for instruction in data:
        direction = instruction[0]
        steps = int(instruction[1:])
        if direction == "F":
            compass[currentFacingDirection] += steps
        elif direction == "E":
            compass["E"] += steps
        elif direction == "S":
            compass["S"] += steps
        elif direction == "W":
            compass["W"] += steps
        elif direction == "N":
            compass["N"] += steps
        elif direction == "R":
            rotation = steps / 90
            idx = directions.index(currentFacingDirection)
            currentFacingDirection = directions[(idx + int(rotation)) % 4]
        elif direction == "L":
            rotation = steps / 90
            idx = directions.index(currentFacingDirection)
            currentFacingDirection = directions[(idx - int(rotation)) % 4]
    ans = abs(compass["E"] - compass["W"]) + abs(compass["N"] - compass["S"])
    print(ans)


def part2():
    currentFacingDirection = directions[0]
    waypoint = {"E": 10, "S": 0, "W": 0, "N": 1}

    for instruction in data:
        direction = instruction[0]
        steps = int(instruction[1:])
        if direction == "F":
            for point in compass:
                compass[point] += steps * waypoint[point]
        elif direction == "E":
            waypoint["E"] += steps
        elif direction == "S":
            waypoint["S"] += steps
        elif direction == "W":
            waypoint["W"] += steps
        elif direction == "N":
            waypoint["N"] += steps
        elif direction == "R":
            rotation = steps / 90
            waypointAlt = dict()
            for k, v in waypoint.items():
                idx = directions.index(k)
                currentFacingDirection = directions[(idx + int(rotation)) % 4]
                waypointAlt[currentFacingDirection] = v
            waypoint = waypointAlt
        elif direction == "L":
            rotation = steps / 90
            waypointAlt = dict()
            for k, v in waypoint.items():
                idx = directions.index(k)
                currentFacingDirection = directions[(idx - int(rotation)) % 4]
                waypointAlt[currentFacingDirection] = v
            waypoint = waypointAlt
    ans = abs(compass["E"] - compass["W"]) + abs(compass["N"] - compass["S"])
    print(ans)


part2()
