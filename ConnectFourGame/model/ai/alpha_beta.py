import math
from ConnectFourGame.model.ai.get_valid_moves import get_valid_moves
from ConnectFourGame.model.ai.evaluation import evaluation
from ConnectFourGame.model.game.winner_checking import check_for_player_win
from ConnectFourGame.model.utils import get_opposite_player


def get_move_with_alpha_beta(board, depth, current_player):
    alpha = -math.inf
    beta = math.inf
    moves = get_valid_moves(board)
    move = -1
    best = -math.inf
    for row, column in moves:
        current_board = copy_array(board)
        current_board[row][column] = current_player
        value = alpha_beta(current_board, depth - 1, alpha, beta,
                           maximizing_player=current_player,
                           current_player=get_opposite_player(current_player),
                           last_move=(row, column))
        if value > best:
            best = value
            move = column
        alpha = max(alpha, best)
        if beta <= alpha:
            break
    return move


def alpha_beta(board, depth, alpha, beta, maximizing_player, current_player, last_move):
    moves = get_valid_moves(board)
    if depth == 0 or not moves \
            or check_for_player_win(board, last_move[0], last_move[1], get_opposite_player(current_player)):
        return evaluation(board, maximizing_player, current_player, last_move)
    if maximizing_player == current_player:
        best = -math.inf
        for row, column in moves:
            current_board = copy_array(board)
            current_board[row][column] = current_player
            value = alpha_beta(current_board, depth - 1, alpha, beta,
                               maximizing_player=maximizing_player,
                               current_player=get_opposite_player(current_player),
                               last_move=(row, column))
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = math.inf
        for row, column in moves:
            current_board = copy_array(board)
            current_board[row][column] = current_player
            value = alpha_beta(current_board, depth - 1, alpha, beta,
                               maximizing_player=maximizing_player,
                               current_player=get_opposite_player(current_player),
                               last_move=(row, column))
            best = min(best, value)
            alpha = min(beta, best)
            if beta <= alpha:
                break
        return best


def copy_array(x):
    return [row[:] for row in x]
