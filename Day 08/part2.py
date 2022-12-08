data = open("input.txt").read().split("\n")

def gowest(r, c):
    trees = 0
    h = int(data[r][c])
    for n in range(int(c), 0, -1):
        t = int(data[r][n-1])
        trees += 1
        if t >= h:
            return trees
    return trees

def goeast(r, c):
    trees = 0
    h = int(data[r][c])
    for n in range(int(c), len(data[r]) - 1):
        t = int(data[r][n+1])
        trees += 1
        if t >= h:
            return trees
    return trees

def gonorth(r, c):
    trees = 0
    h = int(data[r][c])
    for n in range(int(r), 0, -1):
        t = int(data[n-1][c])
        trees += 1
        if t >= h:
            return trees
    return trees

def gosouth(r, c):
    trees = 0
    h = int(data[r][c])
    for n in range(int(r), len(data) - 1):
        t = int(data[n+1][c])
        trees += 1
        if t >= h:
            return trees
    return trees

# 5 and 8

scenics=[]

for row in range(1, len(data[0])-1):
    for col in range(1, len(data)-1):
        scenics.append(gowest(row,col) * goeast(row,col) * gosouth(row,col) * gonorth(row,col))
    
print ("Part 2:", max(scenics))