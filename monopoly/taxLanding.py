def taxLanding(players, property, i, playerAmount):
    print(f"You landed on {property["name"]}. You owe {property["amount"]} in tax.")
    if players[i].money < property["amount"]:
        if len(players[i].properties) == 0:
            print("Tax is greater than your balance. You have no properties you can mortgage. You lose.")
            del players[i]
            return playerAmount - 1
        else:
            print("Tax is greater than your balance. Mortgage a property to pay for tax.")
    players[i].money = players[i].money - property["amount"]
    print(f"Your new balance is {players[i].money}.")
    return playerAmount