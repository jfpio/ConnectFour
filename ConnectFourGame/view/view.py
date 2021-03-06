from ConnectFourGame.model.player.player_token import PlayerToken


class View:
    @staticmethod
    def display_welcome_screen():
        print("Welcome in game in four\n")

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
                    print("[", board[row][col].value, "]", sep="", end="")
            print("")
        print("")

    @staticmethod
    def display_current_turn_player(player_name):
        print("\n")
        print(player_name, "turn:")

    @staticmethod
    def display_winner(winner):
        print(winner, "win")


