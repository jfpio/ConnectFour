from model.player.player_type import PlayerType

class View:

    def __init__(self):
        pass

    @staticmethod
    def display_welcome_screen():
        print("Welcome in game in four\n")

    """Initialize game"""

    @staticmethod
    def get_board_rows():
        print("Choose board rows amount: ")
        return input()

    @staticmethod
    def get_board_cols():
        print("Choose board columns amount: ")
        return input()

    """Initialize player"""

    @staticmethod
    def get_player_type(player):
        print("Player types: \n1. human\n2. ai")
        print("Choose", player, "player type: ")
        current_input = input()
        if current_input == '1':
            return PlayerType.HUMAN
        else:
            return PlayerType.AI

    @staticmethod
    def get_search_depth():
        print("Choose search depth for AI: ")
        return input()

    """Gameplay"""

    def display_board(self, board):
        print("This is board")

    def display_current_turn_player(self, player_name):
        print("\n")
        print(player_name, "turn:")

    def get_human_move(self, cols ):
        print("Choose column from 0 to", cols, "to put token: ")
        return input()


