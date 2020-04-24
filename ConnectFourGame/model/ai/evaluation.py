from ConnectFourGame.model.game.winner_checking import check_for_player_win
from ConnectFourGame.model.utils import get_opposite_player
from ConnectFourGame.model.player.player_token import PlayerToken

SCORE_FOR_WIN = 10000


def evaluation(board, maximizing_player, player, last_move):
    if check_for_player_win(board, last_move[0], last_move[1], player):
        return SCORE_FOR_WIN
    elif check_for_player_win(board, last_move[0], last_move[1], get_opposite_player(maximizing_player)):
        return -SCORE_FOR_WIN
    else:
        return get_score_for_board(board, maximizing_player)


def get_score_for_board(board, maximizing_player):
    score = 0

    score += get_score_for_center(board, maximizing_player)
    score -= get_score_for_center(board, get_opposite_player(maximizing_player))
    number_of_columns = len(board[0])
    number_of_rows = len(board)
    window_length = 4
    for row in range(number_of_rows):
        row_array = [i for i in board[row]]
        for column in range(number_of_columns - 3):
            window = row_array[column:column + window_length]
            score += evaluate_window(window, maximizing_player)

    for column in range(number_of_columns):
        col_array = [row[column] for row in board]
        for row in range(number_of_rows - 3):
            window = col_array[row:row + window_length]
            score += evaluate_window(window, maximizing_player)

    for row in range(number_of_rows - 3):
        for column in range(number_of_columns - 3):
            window = [board[row + i][column + i] for i in range(window_length)]
            score += evaluate_window(window, maximizing_player)

    for row in range(number_of_rows - 3):
        for column in range(number_of_columns - 3):
            window = [board[row + 3 - i][column + i] for i in range(window_length)]
            score += evaluate_window(window, maximizing_player)

    return score


def evaluate_window(window, maximizing_player):
    score = 0
    if window.count(maximizing_player) == 4:
        score += 100
    elif window.count(maximizing_player) == 3 and window.count(PlayerToken.NOBODY) == 1:
        score += 5
    elif window.count(maximizing_player) == 2 and window.count(PlayerToken.NOBODY) == 2:
        score += 2
    if window.count(get_opposite_player(maximizing_player)) == 3 and window.count(PlayerToken.NOBODY) == 1:
        score -= 30
    return score


def get_score_for_center(board, player):
    if len(board) % 2 == 0:
        center_column_left = board[int(len(board)/2 - 1)][:]
        center_column_right = board[int(len(board)/2)][:]
        return (center_column_left.count(player) + center_column_right.count(player)) * 3

    else:
        center_column = board[int(len(board)/2)][:]
        return center_column.count(player) * 3
