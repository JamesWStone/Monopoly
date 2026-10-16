from random import randint

def DiceRoll(d):
    result = randint(1,d)
    print(f"You rolled a {result}")
    rollAgain = str(input("Roll again? Y/N "))
    rollAgain = rollAgain.lower()
    if rollAgain == "y":
        DiceRoll(d)
    
d = int(input("Enter how many sides on the die: "))
DiceRoll(d)