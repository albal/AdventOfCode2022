data = open("input.txt").read().split("\n")

cycle = []
x = 1
cycle.append(1)
cycle.append(1)
for command in data:
    if command == "noop":
        cycle.append(x)
    else:
        v = int(command.split(' ')[1])
        x += v
        cycle.append(x)
        cycle.append(x)

print("Part 1:", cycle[19]*20 + cycle[59]*60 + cycle[99]*100 + cycle[139]*140 + cycle[179]*180 + cycle[219]*220)