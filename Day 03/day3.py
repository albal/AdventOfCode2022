data = open("input3.txt").readlines()


def diff(p1, p2):
    for c in p1:
        if c in p2:
            return c


def value(c):
    val = ord(c)
    if val >= ord("a") and val <= ord("z"):
        return val - ord ("a") + 1
    if val >= ord("A") and val <= ord("Z"):
        return val - ord("A") + 27

def inallthree(l1, l2, l3):
    for c1 in l1:
        if c1 in l2 and c1 in l3:
            return c1


sum = 0

for line in data:
    n = len(line)
    part1 = line[0:n//2].strip()
    part2 = line[n//2:n].strip()
    d = diff(part1, part2)
    v = value(d)
    sum += v 
    

print("Part 1:", sum)

sum = 0
for n in range(0, len(data)-2, 3):
    line1 = data[n].strip()
    line2 = data[n+1].strip()
    line3 = data[n+2].strip()
    ch = inallthree(line1, line2, line3)
    sum += value(ch) 

print("Part 2:", sum)