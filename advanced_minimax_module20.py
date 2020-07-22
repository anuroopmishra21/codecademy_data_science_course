from connect_four import *
print_board(half_done)
select_space(half_done, 6, 'X')
print(tree_size(half_done, 'O'))

from connect_four import *
import random
random.seed(108)
new_board = make_board()
# Add a third parameter named depth
def minimax(input_board, is_maximizing, depth):
  # Change this if statement to also check to see if depth = 0
  if game_is_over(input_board) or depth == 0:
    return [evaluate_board(input_board), ""]
  best_move = ""
  if is_maximizing == True:
    best_value = -float("Inf")
    symbol = "X"
  else:
    best_value = float("Inf")
    symbol = "O"
  for move in available_moves(input_board):
    new_board = deepcopy(input_board)
    select_space(new_board, move, symbol)
    #Add a third parameter to this recursive call
    hypothetical_value = minimax(new_board, not is_maximizing, depth-1)[0]
    if is_maximizing == True and hypothetical_value > best_value:
      best_value = hypothetical_value
      best_move = move
    if is_maximizing == False and hypothetical_value < best_value:
      best_value = hypothetical_value
      best_move = move
  return [best_value, best_move]
print(minimax(new_board, True, 3))

from connect_four import *
import random
random.seed(108)
def evaluate_board(board):
    if has_won(board, "X"):
      return float("Inf")
    elif has_won(board, "O"):
      return -float("Inf")
    else:
      num_top_x = 0
      num_top_o = 0
      for column in board:
        for square in column:
          if square == 'X':
            num_top_x +=1
            break
          if square == 'O':
            num_top_o +=1
            break
      return num_top_x - num_top_o
print_board(board_one)
print_board(board_two)
print_board(board_three)
print(evaluate_board(board_one))
print(evaluate_board(board_two))
print(evaluate_board(board_three))

from connect_four import *
import random
random.seed(108)

def minimax(input_board, is_maximizing, depth, alpha, beta):
  # Base case - the game is over, so we return the value of the board
  if game_is_over(input_board) or depth == 0:
    return [evaluate_board(input_board), "", alpha,  beta]
  best_move = ""
  if is_maximizing == True:
    best_value = -float("Inf")
    symbol = "X"
  else:
    best_value = float("Inf")
    symbol = "O"
  for move in available_moves(input_board):
    new_board = deepcopy(input_board)
    select_space(new_board, move, symbol)
    hypothetical_value = minimax(new_board, not is_maximizing, depth - 1, alpha, beta)[0]
    if is_maximizing == True and hypothetical_value > best_value:
      best_value = hypothetical_value
      best_move = move
      alpha = max(alpha, best_value)
    if is_maximizing == False and hypothetical_value < best_value:
      best_value = hypothetical_value
      best_move = move
      beta = min(beta, best_value)
    if alpha >= beta:
      break
  return [best_value, best_move, alpha, beta]
print_board(board)
print(minimax(board, True, 6, -float('Inf'), float('Inf')))

from connect_four import *
def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      # Fill in the third parameter for the first player's "intelligence"
      result = minimax(my_board, True, 4, -float("Inf"), float("Inf"))
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)
      if not game_is_over(my_board):
        #Fill in the third parameter for the second player's "intelligence"
        result = minimax(my_board, False, 4, -float("Inf"), float("Inf"))
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
