import unittest
from ConnectFourGame.model.ai.alpha_beta import get_move_with_alpha_beta
from ConnectFourGame.model.ai.get_valid_moves import get_valid_moves
from ConnectFourGame.tests.utils import transform_board_for_game
from ConnectFourGame.model.player.player_token import PlayerToken


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

    def test_if_ai_could_block_move_1(self):
        board = [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, -1, 0, 0],
            [1, 0, -1, 0, 0],
        ]
        expected_move = 0
        self.assertEqual(expected_move, get_move_with_alpha_beta(transform_board_for_game(board), 4, PlayerToken.O))

    def test_if_ai_could_block_move_2(self):
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [1, 1, -1, -1, -1],
            [1, -1, -1, -1, 1],
        ]
        expected_move = 3
        self.assertEqual(expected_move, get_move_with_alpha_beta(transform_board_for_game(board), 2, PlayerToken.O))

    def test_if_ai_could_block_move_3(self):
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, -1, 0, 0, -1],
            [1, 1, 1, 0, -1],
        ]
        expected_move = 3
        self.assertEqual(expected_move, get_move_with_alpha_beta(transform_board_for_game(board), 4, PlayerToken.O))
