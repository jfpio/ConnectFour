from ConnectFourGame.model.player.player import Player
from ConnectFourGame.model.utils import get_input_from_range


class HumanPlayer(Player):
    @staticmethod
    def get_move(board):
        # Check if inout is valid
        print("Choose column from 0 to ? to put token: ")
        return get_input_from_range(0, 100)
