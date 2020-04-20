from ConnectFourGame.model.player.constants import PlayerToken
from ConnectFourGame.model.game.game_logic import check_if_sb_could_move, check_for_winner


class Game:
    def __init__(self, columns=7, rows=6):
        self.columns = int(columns)
        self.rows = int(rows)
        self.board = [[PlayerToken.NOBODY for x in range(int(columns))] for y in range(int(rows))]

    def get_board(self):
        return self.board

    def get_columns_amount(self):
        return self.columns

    def get_winner(self):
        return check_for_winner(self.get_board())

    def is_end(self):
        if check_if_sb_could_move(self.board) or check_for_winner(self.get_board()) is not PlayerToken.NOBODY:
            return True
        return False

    def insert(self, column, player_token):
        """Insert the player in the given column."""
        for row in range(start=len(self.board) - 1, stop=-1, step=-1):
            if self.board[row][column] == PlayerToken.NOBODY:
                self.board[row][column] = player_token
