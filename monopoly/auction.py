def auction(playerAmount, players, property, i):
    print("Auction!")
    auctionPrice = property["price"]
    bid = auctionPrice
    highestBid = None
    currentPlayer = i
    invalidPlayers = [i]
    auctioning = True
    bidding = False
    while auctioning:
        if len(invalidPlayers) == playerAmount:
             print("Auction over! No valid players can purchase the property.")
             break

        currentPlayer = (currentPlayer + 1) % len(players)
        
        while currentPlayer in invalidPlayers:
            currentPlayer = (currentPlayer + 1) % len(players)

        if players[currentPlayer].money < property["price"] or players[currentPlayer].money <= highestBid:
            invalidPlayers.append(currentPlayer)
            continue

        asking = True
        print(f"Current player bidding: {players[currentPlayer].name}")
        while asking:
            asking = False
            try:
                playerBidding = input("Do you want to buy this property?\nY/N: ").upper()
                if playerBidding != 'Y' and playerBidding != 'N':
                     raise ValueError
            except ValueError:
                 print("Enter a 'Y' to bid or an 'N' to exit bidding.")
                 asking = True
            if playerBidding == "Y":
                bidding = True
            else:
                invalidPlayers.append(currentPlayer)
        while bidding:
            try:
                bidding = False
                bid = int(input("Enter your bid for the property. Must be greater than previous bid.\n"))
                if bid <= auctionPrice:
                     raise ValueError
            except ValueError:
                bidding = True
                print("Error! Must enter a bid greater than the previous bid.")
        auctionPrice = bid
        print(f"Current auction price: {auctionPrice}.")
        if len(invalidPlayers) == playerAmount - 1:
            for x in range (playerAmount):
                if x in invalidPlayers:
                       continue
                else:
                       auctioning = False
                       players[x].properties.append(property)
                       property["owner"] = players[x].id
                       players[x].money -= bid
                       print(f"{players[x].name} now owns {property["name"]}! They spent {bid} when the original price was {property["price"]}.")

def auctionUtility(playerAmount, players, property, i):
    print("Auction!")
    auctionPrice = property["price"]
    bid = auctionPrice
    currentPlayer = i
    invalidPlayers = [i]
    auctioning = True
    bidding = False
    while auctioning:
        if len(invalidPlayers) == playerAmount:
                print("Auction over! No valid players can purchase the property.")
                break

        currentPlayer = (currentPlayer + 1) % len(players)
        
        while currentPlayer in invalidPlayers:
            currentPlayer = (currentPlayer + 1) % len(players)

        if players[currentPlayer].money < property["price"]:
            invalidPlayers.append(currentPlayer)
            continue

        asking = True
        print(f"Current player bidding: {players[currentPlayer].name}")
        while asking:
            asking = False
            try:
                playerBidding = input("Do you want to buy this property?\nY/N: ").upper()
                if playerBidding != 'Y' and playerBidding != 'N':
                     raise ValueError
            except ValueError:
                 print("Enter a 'Y' to bid or an 'N' to exit bidding.")
                 asking = True
            if playerBidding == "Y":
                bidding = True
            else:
                invalidPlayers.append(currentPlayer)
                
        while bidding:
            try:
                bidding = False
                bid = int(input("Enter your bid for the property. Must be greater than previous bid.\n"))
                if bid <= auctionPrice:
                     raise ValueError
            except ValueError:
                bidding = True
                print("Error! Must enter a bid greater than the previous bid.")
        auctionPrice = bid
        print(f"Current auction price: {auctionPrice}.")
        if len(invalidPlayers) == playerAmount - 1:
            for x in range (playerAmount):
                if x in invalidPlayers:
                       continue
                else:
                       auctioning = False
                       players[x].properties.append(property)
                       property["owner"] = players[x].id
                       players[x].money -= bid
                       print(f"{players[x].name} now owns {property["name"]}! They spent {bid} when the original price was {property["price"]}.")

def auctionStation(playerAmount, players, property, i):
    print("Auction!")
    auctionPrice = property["price"]
    bid = auctionPrice
    currentPlayer = i
    invalidPlayers = [i]
    auctioning = True
    while auctioning:
        if len(invalidPlayers) == playerAmount:
                print("Auction over! No valid players can purchase the property.")
                break

        currentPlayer = (currentPlayer + 1) % len(players)
        
        while currentPlayer in invalidPlayers:
            currentPlayer = (currentPlayer + 1) % len(players)

        if players[currentPlayer].money < property["price"]:
            invalidPlayers.append(currentPlayer)
            continue

        asking = True
        print(f"Current player bidding: {players[currentPlayer].name}")
        while asking:
            asking = False
            try:
                playerBidding = input("Do you want to buy this property?\nY/N: ").upper()
                if playerBidding != 'Y' and playerBidding != 'N':
                     raise ValueError
            except ValueError:
                 print("Enter a 'Y' to bid or an 'N' to exit bidding.")
                 asking = True
            if playerBidding == "Y":
                bidding = True
            else:
                invalidPlayers.append(currentPlayer)
        while bidding:
            try:
                bidding = False
                bid = int(input("Enter your bid for the property. Must be greater than previous bid.\n"))
                if bid <= auctionPrice:
                     raise ValueError
            except ValueError:
                bidding = True
                print("Error! Must enter a bid greater than the previous bid.")
        auctionPrice = bid
        print(f"Current auction price: {auctionPrice}.")
        if len(invalidPlayers) == playerAmount - 1:
            for x in range (playerAmount):
                if x in invalidPlayers:
                       continue
                else:
                       auctioning = False
                       players[x].properties.append(property)
                       property["owner"] = players[x].id
                       players[x].money -= bid
                       print(f"{players[x].name} now owns {property["name"]}! They spent {bid} when the original price was {property["price"]}.")
