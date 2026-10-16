import json


def initBoard():
    with open("spaces.json", encoding="utf-8") as file:
        board = json.load(file) 

    spaces = board["spaces"] # 40 Spaces (Indexed 0-39, 0 is Go, 39 is Mayfair)
    return spaces
