with open('input1.txt', 'r') as file:
    data = file.read().split('\n')

WIN = 6
DRAW = 3
LOSS = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

game_scores = {
    'A X': LOSS + SCISSORS,
    'A Y': DRAW + ROCK,
    'A Z': WIN + PAPER,
    'B X': LOSS + ROCK,
    'B Y': DRAW + PAPER,
    'B Z': WIN + SCISSORS,
    'C X': LOSS + PAPER,
    'C Y': DRAW + SCISSORS,
    'C Z': WIN + ROCK,
}


def didiwin(opp, choice):
    if opp == "A" and choice == "X":  # rock vs rock
        return 3
    if opp == "B" and choice == "Y":  # paper vs paper
        return 3
    if opp == "C" and choice == "Z":  # scissors vs scissors
        return 3
    if opp == "A" and choice == "Y":  # rock vs paper
        return 6
    if opp == "B" and choice == "Z":  # paper vs scissors
        return 6
    if opp == "C" and choice == "X":  # scissors vs rock
        return 6
    return 0


def played(choice):
    if choice == "X":
        return 1
    if choice == "Y":
        return 2
    if choice == "Z":
        return 3
    return 0


total = 0

for play in data:
    opponent, me = play.split(" ")
    score = didiwin(opponent, me)
    score += played(me)
    total += score
print("Part 1 Total score:", total)

total = 0

for play in data:
    opponent, me = play.split(" ")
    score = game_scores.get(play, 0)
    total += score
print("Part 2 Total score:", total)

