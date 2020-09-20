# Making Tic Tac Toe!!

# Step 1: Create Tic Tac Toe Board
# Step 2: Place Pieces Continiously
# Step 3: Check Game End
# Step 4: Finalizing Game (Incorrect user inputs)
# Add is digit here

game_over = False
player_turn = "X"

board = [[" ", " ", " "], 
         [" ", " ", " "], 
         [" ", " ", " "]]

def check_win():
  horizontal_victory = board[row][0] == player_turn and board[row][1] == player_turn and board[row][2] == player_turn

  vertical_victory = board[0][col] == player_turn and board[1][col] == player_turn and board[2][col] == player_turn

  diagonal_neg_victory = board[0][0] == player_turn and board[1][1] == player_turn and board[2][2] == player_turn

  diagonal_pos_victory = board[0][2] == player_turn and board[1][1] == player_turn and board[2][0] == player_turn

  return horizontal_victory or vertical_victory or diagonal_neg_victory or diagonal_pos_victory

while not game_over:
  # Print Board
  print("  0 1 2")
  print(f"0 {board[0][0]}|{board[0][1]}|{board[0][2]}")
  print("  -+-+-")
  print(f"1 {board[1][0]}|{board[1][1]}|{board[1][2]}")
  print("  -+-+-")
  print(f"2 {board[2][0]}|{board[2][1]}|{board[2][2]}")

  # Get User Input
  while True:
    row = input("Please input a row: ")
    col = input("Please input a column: ")
    
    if row.isdigit() and col.isdigit():
      row = int(row)
      col = int(col)
      if row <= 2 and row >= 0 and col <= 2 and col >= 0:
        if board[row][col] == " ":
          break
        else:
          print("Please don't place on a taken field")
      else:
        print("Please input a row and col of 0, 1, or 2")
    else:
      print("Please input and integer for both the row and column")

  board[row][col] = player_turn

  # Check Win
  if check_win():
    game_over = True
    print(f"Player {player_turn} Won!")
    print("  0 1 2")
    print(f"0 {board[0][0]}|{board[0][1]}|{board[0][2]}")
    print("  -+-+-")
    print(f"1 {board[1][0]}|{board[1][1]}|{board[1][2]}")
    print("  -+-+-")
    print(f"2 {board[2][0]}|{board[2][1]}|{board[2][2]}")

  # Change Turn
  if player_turn == "X":
    player_turn = "O"
  elif player_turn == "O":
    player_turn = "X"
