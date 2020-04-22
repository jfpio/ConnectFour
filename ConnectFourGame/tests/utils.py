from ConnectFourGame.model.player.constants import PlayerToken


def transform_board_for_game(board):
    for row in board:
        for i in range(len(row)):
            if row[i] == 1:
                row[i] = PlayerToken.X
            elif row[i] == -1:
                row[i] = PlayerToken.O
            elif row[i] == 0:
                row[i] = PlayerToken.NOBODY
    return board
