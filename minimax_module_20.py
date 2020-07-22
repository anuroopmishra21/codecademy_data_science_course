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
