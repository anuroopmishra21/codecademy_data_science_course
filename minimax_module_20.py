from tic_tac_toe import *
my_board = [
	["1", "2", "X"],
	["4", "5", "6"],
	["7", "8", "9"]
]
select_space(my_board, 5, 'O')
select_space(my_board, 6, 'X')
select_space(my_board, 1, 'O')
select_space(my_board, 9, 'X')
print_board(my_board)
print(has_won(my_board, "X"))

from tic_tac_toe import *
start_board = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]
x_won = [
	["X", "O", "3"],
	["4", "X", "O"],
	["7", "8", "X"]
]
o_won = [
	["O", "X", "3"],
	["O", "X", "X"],
	["O", "8", "9"]
]
tie = [
	["X", "X", "O"],
	["O", "O", "X"],
	["X", "O", "X"]
]
def game_is_over(board):
  if has_won(board, "X") == True:
    return True
  elif has_won(board, "O") == True:
    return True
  elif available_moves(board) == []:
    return True
  else:
    return False
print(game_is_over(start_board))
print(game_is_over(x_won))
print(game_is_over(o_won))
print(game_is_over(tie))
def evaluate_board(board):
  if has_won(board, "X") == True:
    return 1
  elif has_won(board, "O") == True:
    return -1
  else:
    return 0
print(evaluate_board(x_won))
print(evaluate_board(o_won))
print(evaluate_board(tie))

