def viewProperty(board, pos):
    if board[pos]["type"] == "property":
        return "property", board[pos]
    elif board[pos]["type"] == "community_chest":
        return "community_chest", board[pos]
    elif board[pos]["type"] == "go":
        return "go", board[pos]
    elif board[pos]["type"] == "tax":
        return "tax", board[pos]
    elif board[pos]["type"] == "station":
        return "station", board[pos]
    elif board[pos]["type"] == "utility":
        return "utility", board[pos]
    elif board[pos]["type"] == "chance":
            return "chance", board[pos]
    elif board[pos]["type"] == "jail":
            return "jail", board[pos]
    elif board[pos]["type"] == "free_parking":
            return "free_parking", board[pos]
    elif board[pos]["type"] == "go_to_jail":
            return "go_to_jail", board[pos]