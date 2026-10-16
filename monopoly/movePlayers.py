from monopolyDice import rollDice

def movePlayer(player, move):
    posPlayer = player
    maxPos = 39
    newPos = posPlayer + move
    if newPos > maxPos:
        newPos -= 40
    return newPos
