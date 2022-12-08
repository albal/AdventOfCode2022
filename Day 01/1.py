with open('input1.txt', 'r') as file:
    data = file.read().split('\n\n')

max_food = 0

for food in data:
    total_food = 0
    for item in filter(None, food.split('\n')):
        total_food = total_food + int(item)
    if total_food > max_food:
        max_food = total_food

print("Max food: ", max_food)
