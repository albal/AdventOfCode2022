data = open("input4.txt").readlines()


def isinrange(r1, r2):
    r1s, r1e = r1.split("-")
    r2s, r2e = r2.split("-")

    ra1 = range(int(r1s), int(r1e) + 1)
    ra2 = range(int(r2s), int(r2e) + 1)

    set1 = set(ra1)
    set2 = set(ra2)

    if set1.issubset(set2) or set2.issubset(set1):
        return True
    return False


def isoverlap(r1, r2):
    r1s, r1e = r1.split("-")
    r2s, r2e = r2.split("-")

    ra1 = range(int(r1s), int(r1e) + 1)
    ra2 = range(int(r2s), int(r2e) + 1)

    for c in ra1:
        if c in ra2:
            return True
    return False
            
sum = 0

for line in data:
    range1, range2 = line.split(",")
    if isinrange(range1, range2):
        sum += 1
    
print("Part 1:", sum)

sum = 0

for line in data:
    range1, range2 = line.split(",")
    if isoverlap(range1, range2):
        sum += 1
    
print("Part 2:", sum)

