def check_for_player_win(board, player_token):
    if check_horizontal_win(board, player_token) \
            or _check_left_to_right_win(board, player_token) \
            or _check_right_to_left_win(board, player_token) \
            or _check_vertical_win(board, player_token):
        return True
    else:
        return False


def check_horizontal_win(board, player_token):
    row_iter = rows_number = len(board)
    column_iter = columns_number = len(board[0])

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
    return False


def _check_vertical_win(board, player_token):
    row_iter = rows_number = len(board)
    column_iter = columns_number = len(board[0])

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
    return False


def _check_left_to_right_win(board, player_token):
    row_iter = rows_number = len(board)
    column_iter = columns_number = len(board[0])

    tokens_in_line = 1

    for i in range(1, 4):

        if row_iter + i < rows_number and column_iter + i < columns_number:

            if board[row_iter + i][column_iter + i] == player_token:
                tokens_in_line += 1
            else:
                break
        else:
            break
    for i in range(1, 4):

        if row_iter - i >= 0 and column_iter - i >= 0:

            if board[row_iter - i][column_iter - i] == player_token:
                tokens_in_line += 1
            else:
                break
        else:
            break

    if tokens_in_line >= 4:
        return True
    return False


def _check_right_to_left_win(board, player_token):
    row_iter = rows_number = len(board)
    column_iter = columns_number = len(board[0])
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
    return False
