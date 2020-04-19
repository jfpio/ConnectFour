from ConnectFourGame.model.player.constants import PlayerToken


def check_for_player_win(board, player_token):
    if check_horizontal_win(board, player_token) \
            or _check_left_to_right_win(board, player_token) \
            or _check_right_to_left_win(board, player_token) \
            or _check_vertical_win(board, player_token):
        return True
    else:
        return False


# TODO Change this to get board and calculate for any board
def check_horizontal_win(board, player_token):
    row = len(board)
    col = len(board[0])

    tokens_in_line = 1
    for i in range(1, 4):
        if col - i >= 0:
            if board[row][col - i] == player_token:
                tokens_in_line += 1
            else:
                break
        else:
            break

    for i in range(1, 4):
        if col + i < columns:
            if self.board[row][col + i] == player_token:
                tokens_in_line += 1
            else:
                break
        else:
            break

    if tokens_in_line >= 4:
        return True
    return False


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
        return True
    return False


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
        return True
    return False


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
        return True
    return False
