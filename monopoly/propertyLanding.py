from auction import auction

def propertyLanding(players, property, i, playerAmount):
    if property["owner"] == i:
        print("You own this property.")
    elif property["owner"] != "none" and property["owner"] != i:
        owner = property["owner"]
        print(f"You landed on {property["name"]}, you owe {players[owner].name} rent.")
    elif property["owner"] == "none":
        print(f"Property for Sale! Property name: {property["name"]}\n Property cost: {property["price"]}\n Property colour: {property["colour"]}\n Property rent: {property["rent"]}")
        buying = True
        while buying:
            try:
                buy = input("Do you want to buy this property?\nY/N: ").upper()
                buying = False
                if buy != "Y" and buy != "N":
                    raise ValueError
                elif players[i].money < property["price"]:
                    print(f"Insufficient funds! You have {players[i].money} but the property costs {property["price"]}.")
                    print("Auctioning property...")
                    buying = False
                    buy = "N"
            except:
                buying = True
                print("Enter a 'Y' to buy the property or a 'N' to auction the property.")
        if buy == "Y":
            players[i].money = players[i].money - property["price"]
            print(f"New balance: {players[i].money}.")
            players[i].properties.append(property["position"])
            property["owner"] = players[i].id
        else:
            auction(playerAmount, players, property, i)
    return playerAmount