from model.player.player_token import PlayerToken
from model.game.winner import Winner
from model.player.player_id import PlayerId

class Game:
    """Main game function, when everything happens. Our game don'w want to know if players are AI or they are humans"""
    def __init__(self, columns=7, rows=6):
        """Create a new game."""
        self.columns = int(columns)
        self.rows = int(rows)
        self.board = [[PlayerToken.NOBODY for x in range(int(columns))] for y in range(int(rows))]
        self.empty_cells = int(columns) * int(rows)
        self.winner = Winner.NOBODY

    def get_board(self):
        return self.board

    def get_cols_amount(self):
        return self.columns

    def get_winner(self):
        return self.winner

    def is_end(self):
        if self.empty_cells == 0 or self.winner != Winner.NOBODY:
            return 1
        return 0

    def insert(self, col, player):
        """Insert the player in the given column."""
        for row in range(len(self.board) - 1, -1, -1):
            if self.board[row][int(col)] == PlayerToken.NOBODY:
                self.board[row][int(col)] = player.get_token()
                self.empty_cells -= 1

                self._check_horizontal_win(row, col, player)
                self._check_vertical_win(row, col, player)
                self._check_left_to_right_win(row, col, player)
                self._check_right_to_left_win(row, col, player)
                break

    def _check_horizontal_win(self, row_str, col_str, player):
        row = int(row_str)
        col = int(col_str)
        player_token = player.get_token()

        tokens_in_line = 1

        for i in range(1, 4):
            if col - i >= 0:
                if self.board[row][col - i] == player_token:
                    tokens_in_line += 1
                else:
                    break
            else:
                break

        for i in range(1, 4):
            if col + i < self.columns:
                if self.board[row][col + i] == player_token:
                    tokens_in_line += 1
                else:
                    break
            else:
                break

        if tokens_in_line >= 4:
            self._set_winner(player)
        return 0

    def _check_vertical_win(self, row_str, col_str, player):
        row = int(row_str)
        col = int(col_str)
        player_token = player.get_token()

        tokens_in_line = 1
        for i in range(1, 4):

            if row + i < self.rows:

                if self.board[row + i][col] == player_token:
                    tokens_in_line += 1
                else:
                    break
            else:
                break

        if tokens_in_line >= 4:
            self._set_winner(player)
        return 0

    def _check_left_to_right_win(self, row_str, col_str, player):
        row = int(row_str)
        col = int(col_str)
        player_token = player.get_token()

        tokens_in_line = 1

        for i in range(1, 4):

            if row + i < self.rows and col + i < self.columns:

                if self.board[row + i][col + i] == player_token:
                    tokens_in_line += 1
                else:
                    break
            else:
                break

        for i in range(1, 4):

            if row - i >= 0 and col - i >= 0:

                if self.board[row - i][col - i] == player_token:
                    tokens_in_line += 1
                else:
                    break
            else:
                break

        if tokens_in_line >= 4:
            self._set_winner(player)
        return 0

    def _check_right_to_left_win(self, row_str, col_str, player):
        row = int(row_str)
        col = int(col_str)
        player_token = player.get_token()

        tokens_in_line = 1

        for i in range(1, 4):

            if row + i < self.rows and col - i >= 0:

                if self.board[row + i][col - i] == player_token:
                    tokens_in_line += 1
                else:
                    break
            else:
                break

        for i in range(1, 4):

            if row - i >= 0 and col + i < self.columns:

                if self.board[row - i][col + i] == player_token:
                    tokens_in_line += 1
                else:
                    break
            else:
                break

        if tokens_in_line >= 4:
            self._set_winner(player)
        return 0

    def _set_winner(self, player):
        if player.get_id() == PlayerId.FIRST_PLAYER:
            self.winner = Winner.FIRST_PLAYER
        else:
            self.winner = Winner.SECOND_PLAYER

