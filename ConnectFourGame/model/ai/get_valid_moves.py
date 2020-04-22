from ConnectFourGame.model.player.constants import PlayerToken


def get_valid_moves(board):
    order = get_order(board)
    moves = []
    for column in order:
        for row in range(len(board) - 1, -1, -1):
            if board[row][column] == PlayerToken.NOBODY:
                moves.append((row, column))
                break
    return moves


def get_order(board):
    columns_number = len(board[0])
    if columns_number % 2 == 0:
        return get_order_for_even(board)
    else:
        return get_order_for_odd(board)


def get_order_for_even(board):
    columns_number = len(board[0])
    order = []
    left_middle = int(columns_number / 2) - 1
    right_middle = left_middle + 1
    for i in range(right_middle):
        order.append(left_middle)
        order.append(right_middle)
        left_middle -= 1
        right_middle += 1
    return order


def get_order_for_odd(board):
    columns_number = len(board[0])
    middle = int(columns_number / 2)
    order = []

    for i in range(middle + 1):
        if i == 0:
            order.append(middle)
        else:
            order.append(middle - i)
            order.append(middle + i)
    return order
