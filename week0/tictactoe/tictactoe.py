"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0

    for row in board:
        for val in row:
            if val == X:
                count += 1
            elif val == O:
                count -= 1

    return O if count > 0 else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                res.add((i, j))

    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")

    current_player = player(board)
    new_board = deepcopy(board)

    (i, j) = action
    new_board[i][j] = current_player

    return new_board


def check_winner_horizontal(board):
    for rows in board:
        if rows[0] != EMPTY and rows[0] == rows[1] == rows[2]:
            return rows[0]

    return None


def check_winner_vertical(board):
    for i in range(3):
        if board[0][i] != EMPTY and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    return None


def check_winner_diagonal(board):
    if (
        board[0][0] == board[1][1] == board[2][2]
        or board[0][2] == board[1][1] == board[2][0]
    ):
        return board[1][1]

    return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    is_horizontal = check_winner_horizontal(board)
    if is_horizontal:
        return is_horizontal

    is_vertical = check_winner_vertical(board)
    if is_vertical:
        return is_vertical

    is_diagonal = check_winner_diagonal(board)
    if is_diagonal:
        return is_diagonal

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    if all(all(row) for row in board):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    if win == O:
        return -1

    return 0


def max_value(board):
    output_action = board

    if terminal(board):
        return (utility(board), output_action)

    v = -math.inf

    for action in actions(board):
        (min_v, _) = min_value(result(board, action))
        if min_v > v:
            v = min_v
            output_action = action

    return (v, output_action)


def min_value(board):
    output_action = board

    if terminal(board):
        return (utility(board), output_action)

    v = math.inf

    for action in actions(board):
        (max_v, _) = max_value(result(board, action))
        if max_v < v:
            v = max_v
            output_action = action

    return (v, output_action)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    return max_value(board)[1] if current_player == X else min_value(board)[1]
