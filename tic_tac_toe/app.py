from flask import Flask, render_template, request, jsonify
import time
from minimax import minimax, nodes_minimax
from alphabeta import alphabeta, nodes_ab
from utils import get_moves

app = Flask(__name__)

def best_move_minimax(board):
    global nodes_minimax
    nodes_minimax = 0
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

def best_move_ab(board):
    global nodes_ab
    nodes_ab = 0
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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    board = data["board"]

    start = time.time()
    m1 = best_move_minimax(board.copy())
    t1 = time.time() - start

    start = time.time()
    m2 = best_move_ab(board.copy())
    t2 = time.time() - start

    return jsonify({
        "move": m2,
        "minimax_time": t1,
        "alphabeta_time": t2,
        "nodes_minimax": nodes_minimax,
        "nodes_ab": nodes_ab
    })

if __name__ == "__main__":
    app.run(debug=True)
