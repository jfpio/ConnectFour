import unittest

from ConnectFourGame.model.game.winner_checking import check_for_player_win
from ConnectFourGame.model.player.constants import PlayerToken


class TestStringMethods(unittest.TestCase):
    def test_for_winner_true(self):
        board = [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, -1],
            [0, 0, 0, 0],
        ]
        assert check_for_player_win(self.transform_board_for_game(board), PlayerToken.X)

    def test_for_winner_false(self):
        board = [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, -1],
            [0, 0, 0, 0],
        ]
        assert check_for_player_win(self.transform_board_for_game(board), PlayerToken.O)

    @staticmethod
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
