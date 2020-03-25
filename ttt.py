
# To validate moves made by each player
def validate_move(board, player):
  move = int(input("Player "+player+", where to? "))
  while True:
    if not 1 <= move <= 9:
      print('Ivalid option. Please choose the correct position on the board!\n')
      move = int(input("Player "+player+", where to? "))
    elif board[move-1] != ' ':
      print('Position taken by other player. Please try again.\n')
      move = int(input("Player "+player+", where to? "))
    else:
      break
  return move

# To determine if the board is in a win/tie condition after every move - not optimized
def check_board(board, player):
  # convenience function to check 'n' in a row symbols
  def line_checker(type):
    for set in type:
      winning = True
      for i in set:
        if not board[i] == player:
          winning = False
      if winning:
        return True
  
  #row check
  set1 = (0,1,2) 
  set2 = (3,4,5) 
  set3 = (6,7,8)
  rows = [set1, set2, set3]
  
  #column check
  set1 = (0,3,6) 
  set2 = (1,4,7) 
  set3 = (2,5,8)
  cols = [set1, set2, set3]

  #diagonals check
  right_diagonal = [(0,4,8)]
  left_diagonal = [(2,4,6)]
  
  for i in [rows, cols, right_diagonal, left_diagonal ]:
    win = line_checker(i)
    if win:
      return True

# Facilitates a move baing made by the player
def play_move(board, player):
  #validate user input
  validated_move = validate_move(board, player) 
  #place symbol on board
  board[validated_move-1] = player 
  #print board after each turn
  show_board(board) 
  game_check = check_board(board, player)
  if game_check:
    print('Player '+player+" wins!")
    return True
  else:
    return False

# Print board function (ideally should be dynamically generated based on size of board)
def show_board(board):
  print("\n")
  print("Board:       Movement Options:")
  print(board[0] + " | " + board[1] + " | " + board[2] + "    1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "    4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "    7 | 8 | 9")
  print("\n")

# To initialize the game board (ideally should be configurable)
def create_board():
  board = []
  for i in range(0,9):
    board.append(' ')
  return board

# Facilitates an entire game session
def start_new_game(starting_player):
  game_over = False
  board = create_board()
  show_board(board)
  player = starting_player
  number_of_turns = 0

  #begin game loop
  while not game_over:
    game_over = play_move(board, player)
    # take turns between players
    if(player == 'X'):
      player = 'O'
    elif (player == 'O'):
      player = 'X'
    number_of_turns = number_of_turns + 1
    if number_of_turns >= 9:
      print('Game tied! No one wins.')
      game_over = True

# driver function
def main():
  starting_player = input("Welcome to Tic-Tac-Toe. Will X or O play first? ") 
  
  # validate correct player option
  while True:
    if not (starting_player.lower() == "x" or  starting_player.lower()== "o"):
      print('Please choose Player X or O and try again.\n')
      starting_player = input("\nWelcome to Tic-Tac-Toe. Will X or O play first? ")
    else:
      break
  
  # starting prompt
  print('\nPlayers, please make your move selection by entering a number 1-9 corresponding to the movement option on the right.\n')

  starting_player = starting_player.upper()
  start_new_game(starting_player)

# invoke main function
if __name__ == "__main__":
    main()
