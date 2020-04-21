from ConnectFourGame.model.player.constants import Player
from ConnectFourGame.model.game.winner_checking import check_for_player_win


class Game:
    def __init__(self, columns=7, rows=6):
        self.columns = int(columns)
        self.rows = int(rows)
        self.board = [[Player.NOBODY for x in range(int(columns))] for y in range(int(rows))]
        self.empty_cells = columns * rows
        self.winner = Player.NOBODY

    def get_board(self):
        return self.board

    def get_columns_amount(self):
        return self.columns

    def get_winner(self):
        return self.winner

    def is_end(self):
        if self.empty_cells == 0 or self.winner != Player.NOBODY:
            return True
        return False

    def insert(self, column, player_token):
        """Insert the player in the given column."""
        for row in range(len(self.board) - 1, -1, -1):
            if self.board[row][int(column)] == Player.NOBODY:
                self.board[row][int(column)] = player_token
                self.empty_cells -= 1
                if check_for_player_win(board=self.board,
                                        chosen_row=row,
                                        chosen_column=column,
                                        player_token=player_token):
                    self.winner = player_token
                return True
        return False
