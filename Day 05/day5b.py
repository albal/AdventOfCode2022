import re
data = open("input5.txt").readlines()
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
    sf = int(a) - 1
    st = int(b) - 1
    amount = (int(no) - 1) * -1
    val = []
    for n in range(0, int(no)):
        val.append(stack[sf].pop())
    print ("Val:", val, "amount:", amount)
    for c in val[::-1]:
        stack[st].append(c)
sum = 0

ans = ""
for s in stack:
    ans = ans + s[-1]

print("Part 1:", ans)

