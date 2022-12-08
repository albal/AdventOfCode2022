data = open("input.txt").read().split("\n")

def gowest(r, c):
    h = int(data[r][c])
    for n in range(int(c), 0, -1):
        t = int(data[r][n-1])
        if t >= h:
            return False
    return True

def goeast(r, c):
    h = int(data[r][c])
    for n in range(int(c), len(data[r]) - 1):
        t = int(data[r][n+1])
        if t >= h:
            return False
    return True

def gonorth(r, c):
    h = int(data[r][c])
    for n in range(int(r), 0, -1):
        t = int(data[n-1][c])
        if t >= h:
            return False
    return True

def gosouth(r, c):
    h = int(data[r][c])
    for n in range(int(r), len(data) - 1):
        t = int(data[n+1][c])
        if t >= h:
            return False
    return True


# 16 + 5 = 21
vis = len(data[0]) * 2 + (len(data) * 2) - 4

print (vis)
for row in range(1, len(data[0])-1):
    for col in range(1, len(data)-1):
        if gowest(row,col) or goeast(row,col) or gosouth(row,col) or gonorth(row,col):
            vis += 1
    #     print(data[row][col], end="")
    # print("")
    
print("")
print ("Part 1:", vis)

