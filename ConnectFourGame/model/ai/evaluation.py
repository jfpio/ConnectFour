import math
from ConnectFourGame.model.ai.get_valid_moves import get_valid_moves
from ConnectFourGame.model.player.constants import PlayerToken
from ConnectFourGame.model.game.winner_checking import check_for_player_win
from ConnectFourGame.model.utils import get_opposite_player


def evaluation(board, maximizing_player, player):
    if maximizing_player == player:
        return evaluation_for_maximizing_player(board, player)
    else:
        return evaluation_for_minimizing_player(board, player)


def evaluation_for_maximizing_player(board, player):
    move_value = 0
    for next_possible_move in get_valid_moves(board):
        (threes, two, ones) = count_moves(board, player, next_possible_move)


def evaluation_for_minimizing_player(board, player):
    move_value = 0


def count_moves(board, player, move):
    count_in_vertical(board, player, move)
    count_in_horizontal(board, player, move)
    count_from_left_to_right(board, player, move)
    count_from_right_to_left(board, player, move)


def count_in_vertical(board, player, move):
    counter = 1
    (row, column) = move
    if not row - 1 >= 0: # Square above not exist (isn't available in next move)
        return 0    # blocked move
    for i in range(1, 4):
        if not row + i >= len(board) and board[row + i][column] == player:    # It cannot go out of scope and field must belong to player
            counter += 1
        else:
            break
    return counter


def count_in_horizontal(board, player, move):
    counter = 1
    (row, column) = move
    left = True
    right = True
    move_at_left_is_not_useless = True
    move_at_right_is_not_useless = True
    for i in range(1, 4):
        if left:
            if not column - i < 0 and board[row][column - i] == player:
                counter += 1
            elif not column - i < 0 and board[row][column - i] == PlayerToken.NOBODY:
                left = False
            else:
                move_at_left_is_not_useless = False
                left = False
        if right:
            if not column + i >= len(board[0]) and board[row][column + i] == player:
                counter += 1
            elif not column + i >= len(board[0]) and board[row][column + i] == PlayerToken.NOBODY:
                right = False
            else:
                move_at_right_is_not_useless = False
                right = False
    if move_at_left_is_not_useless or move_at_right_is_not_useless:
        return counter
    else:
        return 0


def count_from_left_up_to_right_down(board, player, move):
    counter = 1
    (row, column) = move
    left_up = True
    right_down = True
    move_at_left_up_is_not_useless = True
    move_at_right_down_is_not_useless = True
    for i in range(1, 4):
        if left_up:
            if not column - i < 0 and not row - i < 0 and board[row - i][column - i] == player:
                counter += 1
            elif not column - i < 0 and not row - i < 0 and board[row - i][column - i] == PlayerToken.NOBODY:
                left_up = False
            else:
                move_at_left_up_is_not_useless = False
                left_up = False
        if right_down:
            if not column + i >= len(board[0]) and not row + i >= len(board) and board[row + i][column + i] == player:
                counter += 1
            elif not column + i >= len(board[0]) and not row + i >= len(board) and board[row + i][column + i] == PlayerToken.NOBODY:
                right_down = False
            else:
                move_at_right_down_is_not_useless = False
                right_down = False
    if move_at_left_up_is_not_useless or move_at_right_down_is_not_useless:
        return counter
    else:
        return 0


def count_from_down_left_to_up_right(board, player, move):
    counter = 1
    (row, column) = move
    down_left = True
    up_right = True
    move_at_right_left_is_not_useless = True
    move_at_up_right_is_not_useless = True
    for i in range(1, 4):
        if down_left:
            if not column - i < 0 and not row + i >= len(board) and board[row + i][column - i] == player:
                counter += 1
            elif not column - i < 0 and not row + i >= len(board) and board[row + i][column - i] == PlayerToken.NOBODY:
                down_left = False
            else:
                move_at_right_left_is_not_useless = False
                down_left = False
        if up_right:
            if not column + i >= len(board[0]) and not row - i < 0 and board[row - i][column + i] == player:
                counter += 1
            elif not column + i >= len(board[0]) and not row - i < 0 and board[row - i][column + i] == PlayerToken.NOBODY:
                up_right = False
            else:
                move_at_up_right_is_not_useless = False
                up_right = False
    if move_at_right_left_is_not_useless or move_at_up_right_is_not_useless:
        return counter
    else:
        return 0


def win_evaluation(board, maximizing_player, player, last_move):
    if player == maximizing_player:
        return 10000
    else:
        return -10000