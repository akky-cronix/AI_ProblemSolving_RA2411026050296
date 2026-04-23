from utils import check_winner, is_draw, get_moves

nodes_ab = 0

def reset_ab():
    global nodes_ab
    nodes_ab = 0

def alphabeta(board, alpha, beta, is_max):
    global nodes_ab
    nodes_ab += 1

    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_draw(board):
        return 0

    if is_max:
        value = -1000
        for move in get_moves(board):
            board[move] = "O"
            value = max(value, alphabeta(board, alpha, beta, False))
            board[move] = " "
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = 1000
        for move in get_moves(board):
            board[move] = "X"
            value = min(value, alphabeta(board, alpha, beta, True))
            board[move] = " "
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value
