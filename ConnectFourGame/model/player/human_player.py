from ConnectFourGame.model.player.player import Player
from ConnectFourGame.model.utils import get_input_from_range
from ConnectFourGame.model.game.get_valid_moves import get_valid_moves


class HumanPlayer(Player):
    @staticmethod
    def get_move(board):
        print(f"Choose column from 0 to {len(board[0]) - 1} to put token: ")
        while True:
            column = get_input_from_range(0, 100)
            valid_moves = get_valid_moves(board)
            valid_columns = [move[1] for move in valid_moves]
            if column in valid_columns:
                return column
            else:
                print("Wrong column")
