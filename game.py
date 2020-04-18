from player_tokens import PlayerTokens


class Game:
    """Main game function, when everything happens. Our game don'w want to know if players are AI or they are humans"""
    def __init__(self, columns=7, rows=6):
        """Create a new game."""
        self.columns = columns
        self.rows = rows
        self.board = [[PlayerTokens.NOBODY for x in range(rows)] for y in range(columns)]

    def if_sb_win_or_game_end(self):
        """Check if somebody win or board is full"""
        pass

    def insert(self, column, player):
        """Insert the player in the given column."""
        pass

    def check_for_winner_and_return_him(self):
        """Check the current board for a winner."""
        pass

    def print_board(self):
        """Print the board."""
        print("Hello World")

    def print_winner_and_game_statistics(self):
        """When game ends print all interesting informations"""
        pass

game = Game()
game.print_board()

