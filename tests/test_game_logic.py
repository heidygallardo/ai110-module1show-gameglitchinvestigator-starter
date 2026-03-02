# file: tests/test_game_logic.py 

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    
    # FIXED: check_guess returns a tuple so must unpack it to get the outcome
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
