from .input import get_depth
from .ai import min_max_alpha_beta


def choose_player():
    print("1. human, 2. ai with const depth, 3. ai with changeable depth")
    user_choice = input()
    if user_choice == 1:
        return human_player_move
    # and other options, in python we don't have a switch statement!


def human_player_move(board):
    """User choose column to place token. We must check if place is valid"""
    pass


def ai_player_with_changeable_depth_move(board):
    depth = get_depth()
    chosen_column = min_max_alpha_beta(board, depth)
    return chosen_column


def ai_player_with_const_depth_move(board):
    """I must think how to do this well"""
