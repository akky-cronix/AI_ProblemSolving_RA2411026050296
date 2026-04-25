from collections import deque
from logic import is_valid

# possible moves (civilians, criminals)
moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

def bfs():
    start = (3,3,0)   # (civilians_left, criminals_left, boat_side)
    goal = (0,0,1)

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        c, cr, boat = state

        for m in moves:
            if boat == 0:  # boat on left
                new = (c - m[0], cr - m[1], 1)
            else:          # boat on right
                new = (c + m[0], cr + m[1], 0)

            if is_valid(new[0], new[1]) and new not in visited:
                visited.add(new)
                queue.append((new, path + [new]))

    return []
