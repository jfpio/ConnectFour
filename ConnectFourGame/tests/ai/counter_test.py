import unittest
from ConnectFourGame.model.ai.counting import count_in_vertical, count_in_horizontal,\
    count_from_down_left_to_up_right, count_from_up_left_to_down_right
from ConnectFourGame.model.player.constants import PlayerToken
from ConnectFourGame.tests.utils import transform_board_for_game


class TestCounters(unittest.TestCase):
    def test_count_in_vertical(self):
        expected_counter = 3
        player = PlayerToken.X
        move = (1, 0)
        board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [1, -1, -1, 1],
        ]
        self.assertEqual(expected_counter, count_in_vertical(transform_board_for_game(board), player, move))

    def test_count_in_horizontal_1(self):
        expected_counter = 3
        player = PlayerToken.X
        move = (2, 2)
        board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 0, 0],
            [1, -1, -1, 1],
        ]
        self.assertEqual(expected_counter, count_in_horizontal(transform_board_for_game(board), player, move))

    def test_count_in_horizontal_2(self):
        expected_counter = 0
        player = PlayerToken.X
        move = (3, 2)
        board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 0, -1],
        ]
        self.assertEqual(expected_counter, count_in_horizontal(transform_board_for_game(board), player, move))

    def test_count_in_diagonal_1(self):
        expected_counter = 3
        player = PlayerToken.X
        move = (1, 2)
        board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, -1, 0],
            [1, 1, -1, -1],
        ]
        self.assertEqual(expected_counter, count_from_down_left_to_up_right(transform_board_for_game(board), player, move))

    def test_count_in_diagonal_2(self):
        expected_counter = 0
        player = PlayerToken.X
        move = (1, 2)
        board = [
            [0, 0, 0, -1],
            [0, 0, 0, -1],
            [0, 1, -1, 1],
            [1, 1, -1, -1],
        ]
        self.assertEqual(expected_counter, count_from_down_left_to_up_right(transform_board_for_game(board), player, move))

    def test_count_in_diagonal_3(self):
        expected_counter = 3
        player = PlayerToken.O
        move = (1, 1)
        board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, -1, 0],
            [1, 1, -1, -1],
        ]
        self.assertEqual(expected_counter,
                         count_from_up_left_to_down_right(transform_board_for_game(board), player, move))

    def test_count_in_diagonal_4(self):
        expected_counter = 0
        player = PlayerToken.O
        move = (1, 1)
        board = [
            [1, 0, 0, 0],
            [-1, 0, 0, 0],
            [1, 1, -1, 0],
            [1, 1, -1, -1],
        ]
        self.assertEqual(expected_counter,
                         count_from_up_left_to_down_right(transform_board_for_game(board), player, move))
