import json


def initCards():
    with open("cards.json", encoding="utf-8") as file:
        cards = json.load(file) 

    communityChest = cards["community_chest"]
    chance = cards["chance"]
    return communityChest, chance
