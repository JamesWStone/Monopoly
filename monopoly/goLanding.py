def goLanding(players, property, i, playerAmount):
    players[i].money += property["salary"]
    print(f"{players[i].name} landed on GO! Collect 200 Money.")
    return playerAmount