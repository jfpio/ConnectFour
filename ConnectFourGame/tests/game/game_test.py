import unittest
from random import randint

from ConnectFourGame.model.player.constants import PlayerToken
from ConnectFourGame.model.game.game import Game
from ConnectFourGame.model.player.human_player import HumanPlayer
from ConnectFourGame.model.player.ai_player import AiPlayer
from ConnectFourGame.view.view import View


class TestStringMethods(unittest.TestCase):
    def test_simple_game(self):
        first_player = HumanPlayer(PlayerToken.X)
        second_player = HumanPlayer(PlayerToken.X)
        game = Game(7, 6)

        current_player = first_player
        while not game.is_end():
            if current_player.get_token() == PlayerToken.X:
                move = 0
            else:
                move = 1
            game.insert(move, current_player.get_token())
            current_player = first_player if current_player == second_player else second_player
        self.assertEqual(PlayerToken.X, game.get_winner())

    def test_if_ai_win_with_random_human(self):
        first_player = HumanPlayer(PlayerToken.X)
        second_player = AiPlayer(PlayerToken.O, 5)

        game = Game(7, 6)
        current_player = first_player
        while not game.is_end():
            if current_player.get_token() == PlayerToken.X:
                move = randint(0, 6)
                if not game.insert(move, current_player.get_token()):
                    continue
            else:
                move = current_player.get_move(game.get_board())
                game.insert(move, current_player.get_token())
                View().display_board(game.get_board())
                a = 0
            current_player = first_player if current_player == second_player else second_player
        View().display_board(game.get_board())
        self.assertEqual(PlayerToken.O, game.get_winner())
