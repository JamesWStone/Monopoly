def chestLanding(players, communityChest, i, playerAmount, card):
    print(f"{players[i].name} landed on Community Chest!")

    if card["type"] == "move_to":
        currentPos = players[i].position
        players[i].position = card["destination"]
        if card["direction"] == "forward":
            if currentPos > players[i].position:
                print(f"{players[i].name} passed GO! Collect 200 Money.")
                players[i].money += 200
    if card["type"] == "receive":
        players[i].money += card["amount"]
        print(card["text"])

    return players[i].position