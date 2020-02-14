import random

tries = 100000
outcome = {"wins": 0, "losses": 0}
outcome_switch = {"wins": 0, "losses": 0}

while tries != 0:
    tries -= 1

    cardoor = random.choice([1, 2, 3])
    choice = random.choice([1, 2, 3])

    prize = {}
    prize[cardoor] = "car"

    # Initialize goats
    for d in [1, 2, 3]:
        if d != cardoor:
            prize[d] = "goat"

    #print(prize)
    #print(choice)
    
    # Open a goat door which wasn't contestant's choice
    for d in [1, 2, 3]:
        if d != choice and prize[d] == "goat":
            prize[d] = "open"
            break
            
    # Now switch door so its not 'choice' or an open door
    for d in [1, 2, 3]:
        if d != choice and prize[d] != "open":
            choice_switched = d
            break

    if choice == cardoor:
        outcome["wins"] += 1
    else:
        outcome["losses"] +=1

    if choice_switched == cardoor:
        outcome_switch["wins"] += 1
    else:
        outcome_switch["losses"] +=1 

print(outcome)
ratio = outcome["wins"]/(outcome["wins"]+outcome["losses"])
print(ratio)

print(outcome_switch)
ratio = outcome_switch["wins"]/(outcome_switch["wins"]+outcome_switch["losses"])
print(ratio)