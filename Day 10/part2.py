data = open("input.txt").read().split("\n")

cycle = []
pixels = []
count = 1
x = 1
cycle.append(1)
cycle.append(1)
for command in data:
    count += 1
    if command == "noop":
        cycle.append(x)
        if count == x:
            pixels.append('#')
        else: 
            pixels.append('.')
    else:
        v = int(command.split(' ')[1])
        x += v
        if x in range(count-2, count+3):
            pixels.append('#')
            pixels.append('#')
        else: 
            pixels.append('.')
            pixels.append('.')
        cycle.append(x)
        cycle.append(x)

for l in range(0, 240, 40):
    c = 0
    for n in range (0, 40):
        if c - 2 < cycle[n+l] < c + 2:
            print("#", end="")
        else:
            print(".", end="")
        c += 1
    print("")
