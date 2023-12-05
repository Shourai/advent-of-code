import string

obligatory = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

count = 0
lines = 0
strng = ""

with open("day4-input", "r") as file:
    for line in file:
        if line == "\n":
            lines += 1
            for i in obligatory:
                if i not in strng:
                    lines -= 1
                    break
                elif i == "pid":
                    lst = strng.split(' ')
                    out = dict(e.split(":") for e in lst[:-1])
                    for k in obligatory:
                        if k == "byr" and not (int(out[k]) >= 1920 and int(out[k]) <= 2002):
                            lines -= 1
                            break
                        elif k == "iyr" and not (int(out[k]) >= 2010 and int(out[k]) <= 2020):
                            lines -= 1
                            break
                        elif k == "eyr" and not (int(out[k]) >= 2020 and int(out[k]) <= 2030):
                            lines -= 1
                            break
                        elif k == "hgt":
                            if out[k][-2:] == 'cm':
                                if not (int(out[k][:-2]) >= 150 and int(out[k][:-2]) <= 193):
                                    lines -= 1
                                    break
                            if out[k][-2:] == 'in':
                                if not (int(out[k][:-2]) >= 59 and int(out[k][:-2]) <= 76):
                                    lines -= 1
                                    break
                        elif k == "hcl":
                            if len(out[k][1:]) != 6:
                                lines -= 1
                                break
                            elif not all(c in string.hexdigits for c in out[k][1:]):
                                lines -= 1
                                break
                        elif k == "ecl":
                            m = ["amb", "blu", "brn",
                                 "gry", "grn", "hzl", "oth"]
                            if out[k] not in m:
                                lines -= 1
                                break
                        elif k == "pid" and not len(out[k]) == 9:
                            lines -= 1
                            break

            strng = ""
            continue
        else:
            strng += line.strip()
            strng += ' '

print(lines)
