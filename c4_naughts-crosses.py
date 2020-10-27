rowOne = [' ',' ',' ']
rowTwo = [' ',' ',' ']
rowThree = [' ',' ',' ']

count = 0
moves = []

def boardPlace(lastInput, play):
  if lastInput:
    if play[0] == '1':
      if play[1] == '1':
        rowOne[0] = 'o'
      elif play[1] == '2':
        rowOne[1] = 'o'
      else:
        rowOne[2] = 'o'

    elif play[0] == '2':
      if play[1] == '1':
        rowTwo[0] = 'o'
      elif play[1] == '2':
        rowTwo[1] = 'o'
      else:
        rowTwo[2] = 'o'

    else:
      if play[1] == '1':
        rowThree[0] = 'o'
      elif play[1] == '2':
        rowThree[1] = 'o'
      else:
        rowThree[2] = 'o'

  else:
    if play[0] == '1':
      if play[1] == '1':
        rowOne[0] = 'x'
      elif play[1] == '2':
        rowOne[1] = 'x'
      else:
        rowOne[2] = 'x'

    elif play[0] == '2':
      if play[1] == '1':
        rowTwo[0] = 'x'
      elif play[1] == '2':
        rowTwo[1] = 'x'
      else:
        rowTwo[2] = 'x'

    else:
      if play[1] == '1':
        rowThree[0] = 'x'
      elif play[1] == '2':
        rowThree[1] = 'x'
      else:
        rowThree[2] = 'x'

def checkTaken(moves, lastInput, play):
  check = True

  for move in moves:
    if move == play:
      if lastInput:
        print('You can\'t do that Player 1, That square is already taken. \n')
        check = False
      else:
        print('You can\'t do that Player 2, That square is already taken. \n')
        check = False

    
    if check == False:
      break

  return check


def winCheck():
  gameWon = False

  # Horizontal Checks
  if rowOne == ['o', 'o', 'o'] or rowTwo == ['o', 'o', 'o'] or rowThree == ['o', 'o', 'o']:
    gameWon = True
    print('------------------')
    print('Winner Player One!')
  elif rowOne == ['x', 'x', 'x'] or rowTwo == ['x', 'x', 'x'] or rowThree == ['x', 'x', 'x']:
    gameWon = True
    print('------------------')
    print('Winner Player Two!')

  # Vertical Checks
  columnOne = [rowOne[0], rowTwo[0], rowThree[0]]
  columnTwo = [rowOne[1], rowTwo[1], rowThree[1]]
  columnThree = [rowOne[2], rowTwo[2], rowThree[2]]

  if columnOne == ['o', 'o', 'o'] or columnTwo == ['o', 'o', 'o'] or columnThree == ['o', 'o', 'o']:
    gameWon = True
    print('------------------')
    print('Winner Player One!')
  elif columnOne == ['x', 'x', 'x'] or columnTwo == ['x', 'x', 'x'] or columnThree == ['x', 'x', 'x']:
    gameWon = True
    print('------------------')
    print('Winner Player Two!')
  
  # Diagonal Checks
  topLeftToBottomRight = [rowOne[0], rowTwo[1], rowThree[2]]
  topRightToBottomLeft = [rowOne[2], rowTwo[1], rowThree[0]]

  if topLeftToBottomRight == ['o', 'o', 'o'] or topRightToBottomLeft == ['o', 'o', 'o']:
    gameWon = True
    print('Winner Player One!')
  elif topLeftToBottomRight == ['x', 'x', 'x'] or topRightToBottomLeft == ['x', 'x', 'x']:
    gameWon = True
    print('Winner Player Two!')

  return gameWon


while True:
  if count == 0:
    naughtsInput = input('Player 1, type the position of play (rows, columns)')
    play = naughtsInput.split(', ')
    lastInput = True

  else:
    if lastInput:
      crossesInput = input('Player 2, type the position of play (rows, columns)')
      play = crossesInput.split(', ')
      lastInput = False

    elif lastInput == False:
      naughtsInput = input('Player 1, type the position of play (rows, columns)')
      play = naughtsInput.split(', ')
      lastInput = True

  print()

  if count == 0:
    boardPlace(lastInput, play)
    moves.append(play)

    print(rowOne)
    print(rowTwo)
    print(rowThree)
    print()

  else: 
    check = checkTaken(moves, lastInput, play)

    if check:
      boardPlace(lastInput, play)
      moves.append(play)

      print(rowOne)
      print(rowTwo)
      print(rowThree)
      print()

    if check == False:
      if lastInput:
        lastInput = False
      else:
        lastInput = True


  gameWon = winCheck()

  if gameWon == True:
    print()
    print(rowOne)
    print(rowTwo)
    print(rowThree)
    break

  count += 1