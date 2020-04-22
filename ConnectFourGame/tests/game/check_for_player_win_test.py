import unittest

from ConnectFourGame.model.game.winner_checking import check_for_player_win
from ConnectFourGame.model.player.constants import PlayerToken
from ConnectFourGame.tests.utils import transform_board_for_game


class TestStringMethods(unittest.TestCase):
    def test_for_winner_true(self):
        board = [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, -1],
            [0, 0, 0, 0],
        ]
        assert check_for_player_win(transform_board_for_game(board), 1, 2, PlayerToken.X)

    def test_for_winner_false(self):
        board = [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, -1],
            [0, 0, 0, 0],
        ]
        self.assertFalse(check_for_player_win(transform_board_for_game(board), 1, 2, PlayerToken.O))

