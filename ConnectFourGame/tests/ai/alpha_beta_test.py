import unittest
from ConnectFourGame.model.ai.get_valid_moves import get_valid_moves
from ConnectFourGame.tests.utils import transform_board_for_game


class TestStringMethods(unittest.TestCase):
    def test_get_valid_moves_for_even_board(self):
        expected_moves = [(2, 1), (2, 2), (2, 0), (2, 3)]
        board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, -1, -1, 1],
        ]
        self.assertEqual(expected_moves, get_valid_moves(transform_board_for_game(board)))

    def test_get_valid_moves_for_odd_board(self):
        expected_moves = [(1, 2), (2, 1), (2, 3), (2, 0), (2, 4)]
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, -1, 0, 0],
            [1, -1, -1, 1, 1],
        ]
        self.assertEqual(expected_moves, get_valid_moves(transform_board_for_game(board)))