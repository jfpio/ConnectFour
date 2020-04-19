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
        return self.winner

    def is_end(self):
        if check_if_sb_could_move(self.board) or check_for_winner(self.get_board()) is not PlayerToken.NOBODY:
            return 1
        return 0
    #TODO Change to true and false

    def insert(self, col, player):
        """Insert the player in the given column."""
        for row in range(len(self.board) - 1, -1, -1):
            if self.board[row][int(col)] == PlayerToken.NOBODY:
                self.board[row][int(col)] = player.get_token()
                self.empty_cells -= 1
    # TODO Refactor this