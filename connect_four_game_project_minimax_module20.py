from connect_four import *
import random
def random_eval(board):
  return random.randint(-100,100)
def my_evaluate_board(board):
  if has_won(board, 'X'):
    return float('Inf')
  if has_won(board, 'O'):
    return -float("Inf")
  x_two_streak = 0
  o_two_streak = 0
  for col in range(len(board)-1):
    for row in range(len(board[0])):
      if board[col][row] == board[col+1][row]:
        if board[col][row] == 'X':
          x_two_streak +=1
        if board[col][row] == 'O':
          o_two_streak +=1
  return x_two_streak - o_two_streak
def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      #The "X" player finds their best move.
      result = minimax(my_board, True, 4, -float("Inf"), float("Inf"), my_evaluate_board)
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)
      if not game_is_over(my_board):
        #The "O" player finds their best move
        result = minimax(my_board, False, 4, -float("Inf"), float("Inf"), codecademy_evaluate_board)
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")
two_ai_game()
