import re

data = open("input5.txt").readlines()

cols = 9

stacks = data[:8]
ins = data[10:]
    
stack = []
s = 0
for c in range (1,36,4):
    new_arr = []
    for i in range(0,8):
        val = stacks[i][c]
        if val != ' ':
            new_arr.append(val)
    stack.append(new_arr[::-1])        

### Do Moves
regex = r"move (\d+) from (\d) to (\d)"
for move in ins:
    print(move)
    no, a, b = re.findall(regex, move)[0]
    print (no, a, b)
    for move in range (0, int(no)):
        sf = int(a) - 1
        st = int(b) - 1
        val = stack[sf].pop()
        stack[st].append(val)
sum = 0

ans = ""
for s in stack:
    ans = ans + s[-1]

print("Part 1:", ans)

