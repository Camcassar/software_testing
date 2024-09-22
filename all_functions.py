# all_functions.py

import random

def get_bingo(my_str, bingo, min_val, max_val):
    """Checks if the guess is correct and generates a new bingo number if needed."""
    my_value = int(my_str)
    if my_value < bingo:
        result_str = my_str + " Too small!"
        new_bingo = bingo
    elif my_value > bingo:
        result_str = my_str + " Too big!"
        new_bingo = bingo
    else:
        result_str = my_str + " Bingo!"
        new_bingo = random.randint(min_val, max_val)
    return result_str, new_bingo
