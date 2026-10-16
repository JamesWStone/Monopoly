from random import randint

def rollDice():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    double = False
    if dice1 == dice2:
        double = True
    return dice1, dice2, double