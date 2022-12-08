import numpy as np

with open('input1.txt', 'r') as file:
    data = file.read().split('\n\n')

elves = []


for food in data:
    total_food = 0
    for item in filter(None, food.split('\n')):
        if item != "":
            total_food = total_food + int(item)
        elves.append(total_food)


sortedarr = np.sort(elves)

print("Part 2: ", sortedarr[-1] + sortedarr[-2] + sortedarr[-3])