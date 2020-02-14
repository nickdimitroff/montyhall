import random

tries = 5000
outcome = {"wins": 0, "losses": 0}

while tries != 0:
    tries -= 1

    cardoor = random.choice([1, 2, 3])
    choice = random.choice([1, 2, 3])

    prize = {}
    prize[cardoor] = "car"

    for d in range(1, 4):
        if d != cardoor:
            prize[d] = "goat"

    #print(prize)
    #print("you chose door", choice)
    if choice == cardoor:
        outcome["wins"] += 1
    else:
        outcome["losses"] +=1

print(outcome)
ratio = outcome["wins"]/(outcome["wins"]+outcome["losses"])
print(ratio)