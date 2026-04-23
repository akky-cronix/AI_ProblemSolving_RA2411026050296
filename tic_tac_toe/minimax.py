from utils import check_winner, is_draw, get_moves

nodes_minimax = 0

def minimax(board, is_max):
    global nodes_minimax
    nodes_minimax += 1

    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_draw(board):
        return 0

    if is_max:
        best = -1000
        for move in get_moves(board):
            board[move] = "O"
            best = max(best, minimax(board, False))
            board[move] = " "
        return best
    else:
        best = 1000
        for move in get_moves(board):
            board[move] = "X"
            best = min(best, minimax(board, True))
            board[move] = " "
        return best
