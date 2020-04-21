def check_for_player_win(board, chosen_row, chosen_column, player_token):
    if _check_horizontal_win(board, chosen_row, chosen_column, player_token) \
            or _check_left_to_right_win(board, chosen_row, chosen_column, player_token) \
            or _check_right_to_left_win(board, chosen_row, chosen_column, player_token) \
            or _check_vertical_win(board, chosen_row, chosen_column, player_token):
        return True
    else:
        return False


def _check_horizontal_win(board, chosen_row, chosen_column, player_token):
    row_iter = chosen_row
    column_iter = chosen_column
    columns_number = len(board[0])

    tokens_in_line = 1

    for i in range(1, 4):
        if column_iter - i >= 0:
            if board[row_iter][column_iter - i] == player_token:
                tokens_in_line += 1
            else:
                break
        else:
            break

    for i in range(1, 4):
        if column_iter + i < columns_number:
            if board[row_iter][column_iter + i] == player_token:
                tokens_in_line += 1
            else:
                break
        else:
            break

    if tokens_in_line >= 4:
        return True
    else:
        return False


def _check_vertical_win(board, chosen_row, chosen_column, player_token):
    row_iter = chosen_row
    column_iter = chosen_column
    rows_number = len(board)

    tokens_in_line = 1
    for i in range(1, 4):

        if row_iter + i < rows_number:

            if board[row_iter + i][column_iter] == player_token:
                tokens_in_line += 1
            else:
                break
        else:
            break

    if tokens_in_line >= 4:
        return True
    else:
        return False


def _check_left_to_right_win(board, chosen_row, chosen_column, player_token):
    row = int(chosen_row)
    col = int(chosen_column)
    columns_number = len(board[0])
    rows_number = len(board)

    tokens_in_line = 1

    for i in range(1, 4):

        if row + i < rows_number and col + i < columns_number:

            if board[row + i][col + i] == player_token:
                tokens_in_line += 1
            else:
                break
        else:
            break

    for i in range(1, 4):

        if row - i >= 0 and col - i >= 0:

            if board[row - i][col - i] == player_token:
                tokens_in_line += 1
            else:
                break
        else:
            break

    if tokens_in_line >= 4:
        return True
    else:
        return False


def _check_right_to_left_win(board, chosen_row, chosen_column, player_token):
    row_iter = chosen_row
    column_iter = chosen_column
    columns_number = len(board[0])
    rows_number = len(board)

    tokens_in_line = 1

    for i in range(1, 4):

        if row_iter + i < rows_number and column_iter - i >= 0:

            if board[row_iter + i][column_iter - i] == player_token:
                tokens_in_line += 1
            else:
                break
        else:
            break

    for i in range(1, 4):

        if row_iter - i >= 0 and column_iter + i < columns_number:

            if board[row_iter - i][column_iter + i] == player_token:
                tokens_in_line += 1
            else:
                break
        else:
            break

    if tokens_in_line >= 4:
        return True
    else:
        return False
