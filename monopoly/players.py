class Player(object):
    def __init__(self, id, name, money, position):
        self.id = id # index 0
        self.name = name # index 1
        self.money = money # index 2
        self.position = position # index 3
        self.properties = [] # index 4

    def __repr__(self):
        return (
            f"Player(id={self.id}, name={self.name!r}, "
            f"money={self.money}, position={self.position})"
            f"money={self.properties}, properties={self.properties})"
        )

def initPlayers():
    playerInput = True
    while playerInput == True:
        try:
            playerAmount = int(input("How many players are playing? \n"))
            playerInput = False
            if playerAmount < 2 or playerAmount > 6:
                playerInput = True
                print("Enter 2-6 players")
        except:
            playerInput = True
            print("Enter 2-6 players")
    players = []
    for i in range(playerAmount):
        name = input(f"Player {i+1}, what is your name? \n")
        players.append(Player(i, name, 1500, 0))
    return players, playerAmount

