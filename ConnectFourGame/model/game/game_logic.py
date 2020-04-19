from ConnectFourGame.model.player.constants import PlayerToken
from ConnectFourGame.model.game.winner_checking import check_for_player_win


def check_for_winner(board):
    if check_for_player_win(board, PlayerToken.X):
        return PlayerToken.X
    elif check_for_player_win(board, PlayerToken.O):
        return PlayerToken.O
    else:
        return PlayerToken.NOBODY


def check_if_sb_could_move(board):
    for column in board:
        for row in board:
            if board[column][row] == PlayerToken.NOBODY:
                return True
    return False
