def chanceLanding(players, card, i, playerAmount):
    print(f"{players[i].name} landed on Chance!")
    for action in card["actions"]:
        if action["type"] == "move_to":
            currentPos = players[i].position
            players[i].position == action["destination"]
            if action["direction"] == "forward":
                if currentPos > players[i].position:
                    print(f"{players[i].name} passed GO! Collect 200 Money.")
                    players[i].money += 200
        elif action["type"] == "receive":
            players[i].money += action["amount"]
            print(card["text"])

    return players[i].position
