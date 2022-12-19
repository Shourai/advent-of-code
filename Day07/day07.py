from dataclasses import dataclass

with open("./testinput", "r") as input:
    input = input.read().splitlines()


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str


@dataclass
class Filesystem:
    dir: Directory
    file: File


workingdir = {"current": "", "previous": ""}
filesystem = list()

for line in input:
    if "cd .." in line:
        workingdir["previous"] = workingdir["current"]
    elif "cd" in line:
        workingdir["previous"] = workingdir["current"]
        workingdir["current"] = line.split()[-1]
    if "ls" in line:
        continue
    if "dir" in line:
        filesystem.append(Directory(line.split()[-1]))
    elif "$" not in line:
        filesystem.append(File(
            line.split()[-1], int(line.split()[0])))

print(filesystem)
