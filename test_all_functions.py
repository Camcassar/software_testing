# test_all_functions.py

import pytest
from all_functions import get_bingo

def test_get_bingo_small():
    result_str, new_bingo = get_bingo("5", 10, 0, 100)
    assert result_str == "5 Too small!"
    assert new_bingo == 10  # bingo number should not change if the guess is wrong

def test_get_bingo_big():
    result_str, new_bingo = get_bingo("15", 10, 0, 100)
    assert result_str == "15 Too big!"
    assert new_bingo == 10  # bingo number should not change if the guess is wrong

def test_get_bingo_bingo():
    result_str, new_bingo = get_bingo("10", 10, 0, 100)
    assert result_str == "10 Bingo!"
    assert 0 <= new_bingo <= 100  # new bingo number should be within the range (0 to 100)

def test_get_bingo_new_range():
    result_str, new_bingo = get_bingo("100", 100, 100, 1000)
    assert result_str == "100 Bingo!"
    assert 100 <= new_bingo <= 1000  # new bingo number should be within the new range (100 to 1000)
