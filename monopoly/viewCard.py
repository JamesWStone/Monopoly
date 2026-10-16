from random import randint

def viewCard(board, pos, communityChest, chance):
    cardId = randint(0, 15)
    if board[pos]["type"] == "community_chest":
        card = communityChest[cardId]
        return card
    if board[pos]["type"] == "chance":
        card = chance[cardId]
        return card
    else:
        return None