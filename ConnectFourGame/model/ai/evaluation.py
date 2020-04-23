from ConnectFourGame.model.ai.get_valid_moves import get_valid_moves
from ConnectFourGame.model.ai.counting import count_moves
from ConnectFourGame.model.game.winner_checking import check_for_player_win

SCORE_FOR_BLOCKED_MOVE = 0
SCORE_FOR_ONE = 5
SCORE_FOR_TWO = 10
SCORE_FOR_THREE = 30
SCORE_FOR_WIN = 10000

# TODO Something is wrong!

def evaluation(board, maximizing_player, player):
    if maximizing_player == player:
        return evaluation_for_maximizing_player(board, player)
    else:
        return evaluation_for_minimizing_player(board, player)


def evaluation_for_maximizing_player(board, player):
    score = 0
    counter_list = [0 for i in range(5)]
    for next_possible_move in get_valid_moves(board):
        if check_for_player_win(board, next_possible_move[0], next_possible_move[1], player):
            score += SCORE_FOR_WIN
        counter_list = sum_values_from_two_list_with_same_len(count_moves(board, player, next_possible_move),
                                                              counter_list)
    score += counter_list[0] * SCORE_FOR_BLOCKED_MOVE
    score += counter_list[1] * SCORE_FOR_ONE
    score += counter_list[2] * SCORE_FOR_TWO
    score += counter_list[3] * SCORE_FOR_THREE
    return score


def evaluation_for_minimizing_player(board, player):
    score = 0
    counter_list = [0 for i in range(4)]
    for next_possible_move in get_valid_moves(board):
        if check_for_player_win(board, next_possible_move[0], next_possible_move[1], player):
            score -= SCORE_FOR_WIN
        counter_list = sum_values_from_two_list_with_same_len(count_moves(board, player, next_possible_move),
                                                              counter_list)
    score -= counter_list[0] * SCORE_FOR_BLOCKED_MOVE
    score -= counter_list[1] * SCORE_FOR_ONE
    score -= counter_list[2] * SCORE_FOR_TWO
    score -= counter_list[3] * SCORE_FOR_THREE
    return score


def sum_values_from_two_list_with_same_len(first_array, second_array):
    new_list = first_array[:]
    for i in range(len(first_array)):
        new_list[i] = first_array[i] + second_array[i]
    return new_list
