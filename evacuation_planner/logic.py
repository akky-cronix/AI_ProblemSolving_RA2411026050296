def is_valid(c_left, cr_left):
    # total = 3 civilians, 3 criminals
    if c_left < 0 or cr_left < 0 or c_left > 3 or cr_left > 3:
        return False

    # Left side constraint
    if c_left > 0 and cr_left > c_left:
        return False

    # Right side constraint
    c_right = 3 - c_left
    cr_right = 3 - cr_left
    if c_right > 0 and cr_right > c_right:
        return False

    return True
