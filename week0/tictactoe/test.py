import tictactoe

board = tictactoe.initial_state()
board[0][0] = "X"
board[0][1] = "X"
board[0][2] = "O"

board[1][0] = "O"
board[1][1] = "X"
# board[1][2] = "X"

board[2][0] = "X"
# board[2][1] = "O"
board[2][2] = "O"
print(board[0])
print(board[1])
print(board[2])
print(tictactoe.player(board))
print(tictactoe.minimax(board))
