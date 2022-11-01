def check_result(board):
    result = False
    pieces = ["x", "o"]
    if " " not in board:
        result = "d"
        return "d"

    wincombos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                 [0, 3, 6], [1, 4, 7], [2, 5, 8],
                 [0, 4, 8], [2, 4, 6]]

    for piece in pieces:
        for wincombo in wincombos:
            if (board[wincombo[0]], board[wincombo[1]], board[wincombo[2]]) == (piece, piece, piece):
                return piece

def minimax(board, isMax):
    result = check_result(board)
    if result == "x":
        return -10
    elif result == "o":
        return 10
    elif result == "d":
        return 0
    
    if isMax:
        score = -1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "o"
                minimax_score = minimax(board, False)
                score = max(score, minimax_score)
                board[i] = " "
        return score

    else:
        score = 1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "x"
                minimax_score = minimax(board, True)
                score = min(score, minimax_score)
                board[i] = " "
        return score 
        
def move(board):
    board = board.copy()
    score = -1000
    bestMove = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "o"
            minimax_score = minimax(board, False)
            if minimax_score > score:
                score = minimax_score
                bestMove = i
            board[i] = " "
    return bestMove