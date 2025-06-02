# Things that still need to be done:
# create a way to reduce points (mistakes happen)
# if it's the last set, play up to 15

def new_game():
    teama = input("Write the name of Team A: ")
    teamb = input("Write the name of Team B: ")
    bestOf = input("Write the total number of sets: ")
    teamA = {"name": teama, "score": 0, "sets": 0}
    teamB = {"name": teamb, "score": 0, "sets": 0}

    print("Match begins...")
    while teamA["sets"] < (int(bestOf)//2)+1 and teamB["sets"] < (int(bestOf)//2)+1:
        print("~"*20 +
              f'\n{teamA["name"]}: {teamA["score"]} ({teamA["sets"]})\n{teamB["name"]}: {teamB["score"]} ({teamB["sets"]})' +
              "\n" + "~"*20)
        nextPoint = input(f"Who scored the next point?\nPress a for {teamA['name']}, b for {teamB['name']}.")
        if nextPoint == "a":
            teamA["score"] += 1
        elif nextPoint == "b":
            teamB["score"] += 1
        else:
            print("The only valid options are: 'a' and 'b'.")
            continue

        if teamA["score"]>=25 or teamB["score"]>=25:
            if teamA["score"]-teamB["score"] >= 2:
                print(f"{teamA['name'].capitalize()} win the set!")
                teamA["sets"] += 1
                teamA["score"] = 0
                teamB["score"] = 0
                continue
            elif teamA["score"]-teamB["score"] <= -2:
                print(f"{teamB['name'].capitalize()} win the set!")
                teamB["sets"] += 1
                teamA["score"] = 0
                teamB["score"] = 0
                continue
            else:
                continue
    if teamA["sets"] == (int(bestOf)//2)+1:
        print(f"{teamA['name'].capitalize()} win the match!\n"
              f"{teamA['name']}: {teamA['sets']}\n"
              f"{teamB['name']}: {teamB['sets']}")
    else:
        print(f"{teamB['name'].capitalize()} win the match!\n"
              f"{teamA['name']}: {teamA['sets']}\n"
              f"{teamB['name']}: {teamB['sets']}")

new_game()