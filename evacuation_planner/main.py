from logic import is_valid
from interactive import suggest_next_move

state = (3,3,0)  # (civilians_left, criminals_left, boat_side)

while True:
    print("\nCurrent State:", state)

    if state == (0,0,1):
        print("✅ All people safely evacuated!")
        break

    try:
        c_move = int(input("Enter civilians to move: "))
        cr_move = int(input("Enter criminals to move: "))
    except:
        print("Invalid input!")
        continue

    c, cr, boat = state

    if boat == 0:
        new_state = (c - c_move, cr - cr_move, 1)
    else:
        new_state = (c + c_move, cr + cr_move, 0)

    if is_valid(new_state[0], new_state[1]):
        state = new_state
    else:
        print("❌ Invalid move!")
        suggestion = suggest_next_move(state)
        print("👉 Suggested next move:", suggestion)
