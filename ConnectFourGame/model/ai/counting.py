from ConnectFourGame.model.player.constants import PlayerToken


def count_moves(board, player, move):
    results = [0 for i in range(4)]

    results[count_in_vertical(board, player, move)] += 1
    results[count_in_horizontal(board, player, move)] += 1
    results[count_from_down_left_to_up_right(board, player, move)] += 1
    results[count_from_up_left_to_down_right(board, player, move)] += 1
    return results


def count_in_vertical(board, player, move):
    counter = 1
    (row, column) = move
    if not row - 1 >= 0:  # Square above not exist (isn't available in next move)
        return 0  # blocked move
    for i in range(1, 4):
        if not row + i >= len(board) and board[row + i][column] == player:  # It cannot go out of scope and field
            # must belong to player
            counter += 1
        else:
            break
    return counter


def count_in_horizontal(board, player, move):
    counter = 1
    (row, column) = move
    left = True
    right = True
    move_at_left_is_not_useless = True
    move_at_right_is_not_useless = True
    for i in range(1, 4):
        if left:
            if not column - i < 0 and board[row][column - i] == player:
                counter += 1
            elif not column - i < 0 and board[row][column - i] == PlayerToken.NOBODY:
                left = False
            else:
                move_at_left_is_not_useless = False
                left = False
        if right:
            if not column + i >= len(board[0]) and board[row][column + i] == player:
                counter += 1
            elif not column + i >= len(board[0]) and board[row][column + i] == PlayerToken.NOBODY:
                right = False
            else:
                move_at_right_is_not_useless = False
                right = False
    if move_at_left_is_not_useless or move_at_right_is_not_useless:
        return counter
    else:
        return 0


def count_from_up_left_to_down_right(board, player, move):
    counter = 1
    (row, column) = move
    left_up = True
    right_down = True
    move_at_left_up_is_not_useless = True
    move_at_right_down_is_not_useless = True
    for i in range(1, 4):
        if left_up:
            if not column - i < 0 and not row - i < 0 and board[row - i][column - i] == player:
                counter += 1
            elif not column - i < 0 and not row - i < 0 and board[row - i][column - i] == PlayerToken.NOBODY:
                left_up = False
            else:
                move_at_left_up_is_not_useless = False
                left_up = False
        if right_down:
            if not column + i >= len(board[0]) and not row + i >= len(board) and board[row + i][column + i] == player:
                counter += 1
            elif not column + i >= len(board[0]) and not row + i >= len(board) \
                    and board[row + i][column + i] == PlayerToken.NOBODY:
                right_down = False
            else:
                move_at_right_down_is_not_useless = False
                right_down = False
    if move_at_left_up_is_not_useless or move_at_right_down_is_not_useless:
        return counter
    else:
        return 0


def count_from_down_left_to_up_right(board, player, move):
    counter = 1
    (row, column) = move
    down_left = True
    up_right = True
    move_at_right_left_is_not_useless = True
    move_at_up_right_is_not_useless = True
    for i in range(1, 4):
        if down_left:
            if not column - i < 0 and not row + i >= len(board) and board[row + i][column - i] == player:
                counter += 1
            elif not column - i < 0 and not row + i >= len(board) and board[row + i][column - i] == PlayerToken.NOBODY:
                down_left = False
            else:
                move_at_right_left_is_not_useless = False
                down_left = False
        if up_right:
            if not column + i >= len(board[0]) and not row - i < 0 and board[row - i][column + i] == player:
                counter += 1
            elif not column + i >= len(board[0]) and not row - i < 0 and board[row - i][
                column + i] == PlayerToken.NOBODY:
                up_right = False
            else:
                move_at_up_right_is_not_useless = False
                up_right = False
    if move_at_right_left_is_not_useless or move_at_up_right_is_not_useless:
        return counter
    else:
        return 0
