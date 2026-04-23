def check_winner(board):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for state in win_states:
        if board[state[0]] == board[state[1]] == board[state[2]] != " ":
            return board[state[0]]
    return None

def is_draw(board):
    return " " not in board

def get_moves(board):
    return [i for i in range(9) if board[i] == " "]
