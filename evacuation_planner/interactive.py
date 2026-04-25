from bfs import bfs

def suggest_next_move(current_state):
    path = bfs()

    for i in range(len(path)-1):
        if path[i] == current_state:
            return path[i+1]

    return None
