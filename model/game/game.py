from model.player.player_token import PlayerToken


class Game:
    """Main game function, when everything happens. Our game don'w want to know if players are AI or they are humans"""
    def __init__(self, columns=7, rows=6):
        """Create a new game."""
        self.columns = int(columns)
        self.rows = int(rows)
        self.board = [[PlayerToken.NOBODY for x in range(int(rows))] for y in range(int(columns))]

    def insert(self, column, player):
        """Insert the player in the given column."""
        print(column, player.token)
        pass

    def get_board(self):
        return self.board

    def get_cols_amount(self):
        return self.columns

    def is_end(self):
        return 0



