from flask import Flask, render_template, request, jsonify
import time

from minimax import minimax, nodes_minimax, reset_minimax
from alphabeta import alphabeta, nodes_ab, reset_ab
from utils import get_moves

app = Flask(__name__)

# ------------------ BEST MOVE (MINIMAX) ------------------
def best_move_minimax(board):
    best_val = -1000
    move = -1

    for i in get_moves(board):
        board[i] = "O"
        val = minimax(board, False)
        board[i] = " "
        if val > best_val:
            best_val = val
            move = i

    return move


# ------------------ BEST MOVE (ALPHA-BETA) ------------------
def best_move_ab(board):
    best_val = -1000
    move = -1

    for i in get_moves(board):
        board[i] = "O"
        val = alphabeta(board, -1000, 1000, False)
        board[i] = " "
        if val > best_val:
            best_val = val
            move = i

    return move


# ------------------ ROUTES ------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/move", methods=["POST"])
def move():
    data = request.json
    board = data["board"]

    # ---- MINIMAX ----
    reset_minimax()
    start = time.time()
    m1 = best_move_minimax(board.copy())
    t1 = time.time() - start
    nodes_m = nodes_minimax

    # ---- ALPHA-BETA ----
    reset_ab()
    start = time.time()
    m2 = best_move_ab(board.copy())
    t2 = time.time() - start
    nodes_a = nodes_ab

    return jsonify({
        "move": m2,  # using Alpha-Beta move
        "minimax_time": t1,
        "alphabeta_time": t2,
        "nodes_minimax": nodes_m,
        "nodes_ab": nodes_a
    })


# ------------------ RUN APP ------------------
if __name__ == "__main__":
    app.run(debug=True)
