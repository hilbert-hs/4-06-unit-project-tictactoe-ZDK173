# Tic-Tac-Toe
import math
board = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

# ###################Glabal Variables####################
turn = 1
player = 'X'
winner = ''

# ###################Win Conditions#####################
def checkHorizontal(board):
  for i in range(0,len(board)):
    if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
      return(board[i][0])
    
  return('')

def checkVertical(board):
  for i in range(0,len(board)):
    if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
      return(board[0][i])
    
  return('')

def checkDiangnal(board):
  row1 = board[0]
  row2 = board[1]
  row3 = board[2]
  if row1[0] == row2[1] and row2[1] == row3[2]:
    return(row1[0])
  else:
    if row1[2] == row2[1] and row2[1] == row3[0]:
      return(row1[2])
  return('')

print()
for row in board:
  print(row)
print()

# ###################Game Loop#####################

while not winner and turn < 10:

    if turn % 2 == 0:
      player = 'O'
    else:
      player = 'X'

    move = int(input(f'Where would you like to place you {player}? '))
    
    #  convert to x y cords
    y = (move % (len(board[0])) - 1)
    x = (math.ceil(move / len(board[y])) - 1)

    if board[x][y] in ['X','O'] or board[x][y] not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
      print("That spot is not availible.")
    else:
      board[x][y] = player

      # Display Board
      print()
      for row in board:
        print(row)
      print()
      # Check Horizontal
      if checkHorizontal(board):
        winner = checkHorizontal(board)
        print(f'{winner} wins!')
      # Check Vertical
      if checkVertical(board):
        winner = checkVertical(board)
        print(f'{winner} wins!')
      # Check Diangonal
      if checkDiangnal(board):
        winner = checkDiangnal(board)
        print(f'{winner} wins!')
      turn += 1

if not winner:
    print("Its a draw.")
    