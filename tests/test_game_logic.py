# file: tests/test_game_logic.py 

from logic_utils import check_guess
from logic_utils import update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win

    # FIXED: fixed logic using AI to ensure that test case is written as intended
    result, message = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, message = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, message = check_guess(40, 50)
    assert result == "Too Low"

def test_too_high_message_says_go_lower():
    # When guess is above secret, player should be told to go LOWER
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_too_low_message_says_go_higher():
    # When guess is below secret, player should be told to go HIGHER
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message



# TEST UPDATE SCORE LOGIC
def test_too_high_even_attempt_penalizes():
    # Previously added 5 points on even attempts — should now subtract
    result = update_score(100, "Too High", 2)
    assert result == 95

def test_too_high_odd_attempt_penalizes():
    result = update_score(100, "Too High", 3)
    assert result == 95

def test_too_low_penalizes():
    result = update_score(100, "Too Low", 1)
    assert result == 95

def test_win_adds_points():
    result = update_score(0, "Win", 1)
    assert result > 0

def test_win_score_floors_at_10():
    # Very late win should still award at least 10 points
    result = update_score(0, "Win", 20)
    assert result == 10