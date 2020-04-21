from ConnectFourGame.model.player.constants import Player


def transform_board_for_game(board):
    for row in board:
        for i in range(len(row)):
            if row[i] == 1:
                row[i] = Player.X
            elif row[i] == -1:
                row[i] = Player.O
            elif row[i] == 0:
                row[i] = Player.NOBODY
    return board
