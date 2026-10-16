from players import initPlayers
from board import initBoard
from monopolyDice import rollDice
from movePlayers import movePlayer
from viewProperty import viewProperty
from cards import initCards
from landingHandler import landingHandler
from viewCard import viewCard

players, playerAmount = initPlayers()
board = initBoard()
communityChest, chance = initCards()

def game(players, board, playerAmount):
    turn = 0
    playing = True
    while playing:
        for i in range(playerAmount):
            turn += 1
            print(f"{players[i].name}'s turn!")
            print("Rolling dice...")
            roll1, roll2, double = rollDice()
            print(f"You rolled a {roll1} and a {roll2}.")
            move = roll1 + roll2
            players[i].position = movePlayer(players[i].position, move)
            if double:
                print("Double!")
            propertyType, property = viewProperty(board, players[i].position)
            card = viewCard(board, players[i].position, communityChest, chance)
            playerAmount = landingHandler(propertyType, players, i, playerAmount, property, card)

game(players, board, playerAmount)