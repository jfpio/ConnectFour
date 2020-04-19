from model.player.player_type import PlayerType
from model.player.player_token import PlayerToken
class View:

    def __init__(self):
        pass

    @staticmethod
    def display_welcome_screen():
        print("Welcome in game in four\n")

    """Initialize game"""

    @staticmethod
    def get_board_rows():
        print("Choose board rows amount: ", end="")
        return input()

    @staticmethod
    def get_board_cols():
        print("Choose board columns amount: ",  end="")
        return input()

    """Initialize player"""

    @staticmethod
    def get_player_type(player):
        print("Player types: \n1. human\n2. ai")
        print("Choose", player, "player type: ", end="")
        current_input = input()
        if current_input == '1':
            return PlayerType.HUMAN
        else:
            return PlayerType.AI

    @staticmethod
    def get_search_depth():
        print("Choose search depth for AI: ", end="")
        return input()

    """Gameplay"""

    @staticmethod
    def display_board(board):
        for col in range(len(board[0])):
            if col >= 10:
                print(col, "", end="")
            else:
                print("", col, "", end="")
        print("")
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == PlayerToken.NOBODY:
                    print("[ ]", end="")
                else:
                    print("[", board[row][col], "]", sep="", end="")
            print("")
        print("")

    @staticmethod
    def display_current_turn_player(player_name):
        print("\n")
        print(player_name, "turn:")

    @staticmethod
    def get_human_move(cols):
        print("Choose column from 0 to", cols, "to put token: ", end="")
        return input()

    """End"""

    @staticmethod
    def display_winner(winner):
        print(winner, "win")


