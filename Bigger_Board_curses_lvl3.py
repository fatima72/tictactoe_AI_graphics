import curses, time
def printboard(height, width):
    '''  
          The Function to print a cell of a board
 
          params:
               Height , Width positioning of screen where cell is to be printed
               height : Integer
               width : Integer
                                  '''
    for i in range(5):
        stdscr.addstr(i + height , width, '|                    |\n')
        stdscr.refresh()
    height = height + 5
    stdscr.addstr(height, width, '----------------------\n')
    stdscr.refresh()
 
def printcross(height, width):
     '''
     The Function to print Cross in a cell
   
      params:
               Height , Width positioning of screen from where cell starts to print
               height : Integer
               width : Integer
                                  '''
     stdscr.addstr(height, width, '|   **        **     |')
     stdscr.addstr(height + 1, width, '|     **   **        |')
     stdscr.addstr(height + 2, width, '|        *           |')
     stdscr.addstr(height + 3, width, '|     **   **        |')
     stdscr.addstr(height + 4, width, '|   **       **      |')
     height = height + 5
     stdscr.addstr(height, width, '----------------------\n')
     stdscr.refresh()
 
def printzero(height, width):
    '''
     The Function to print Zero in a cell
   
      params:
               Height , Width positioning of screen from where cell starts to print
               Height : Integer
               Width : Integer
                                  '''
    stdscr.addstr(height, width, '|      #####         |')
    stdscr.addstr(height + 1, width, '|   ##       ##      |')
    stdscr.addstr(height + 2, width, '|  ##         ##     |')
    stdscr.addstr(height + 3, width, '|   ##       ##      |')
    stdscr.addstr(height + 4, width, '|      #####         |')
    height = height + 5
    stdscr.addstr(height, width, '----------------------\n')
    stdscr.refresh()
 
def update_board(z):
    '''
     The function to update board after every move
 
     params :
           a list Z containg location of moves of player 1 (X) and Player 2 (O)
            z : 2D List  
    '''
           
       
    height = 1
    width = 0
    for i in range(3):
        for j in range(3):
            if (z[i][j] == 'O'):
                printzero(height, width)
            elif(z[i][j] == 'X'):
                printcross(height, width)
            else:
                printboard(height, width)
            width = width + 22
        height= height + 6
        width = 0
 
 
def game(z, choices):
   '''
   The function deciding the main flow of game
 
   params:
          z and Choices list containing moves of both player one used to update board and other to decide the winner 
          z : 2D List
          choices : 2D List
   '''
   flag = 0
   winner = False
   while not winner and flag<=8:
      if flag%2 == 0:
          stdscr.addstr(20, 0, 'Player 1 Turn : ')
      else:
          stdscr.addstr(20, 0, 'Player 2 Turn : ')
      a = stdscr.getstr(22, 0, 3).decode(encoding="utf-8")
      stdscr.addstr(22, 0, '                                    ')
      stdscr.refresh()
      stdscr.addstr(24, 0, '                                       ')
      stdscr.refresh()
      try:
         row = int(a[0])
         column = int(a[2])
      except:
         stdscr.addstr(24, 0, 'wrong input try again')
         stdscr.refresh()
         continue
      if a[1] != ' ' or row > 2 or column > 2:
         stdscr.addstr(24, 0, 'wrong input try again')
         stdscr.refresh()
         continue
      if choices[row][column] not in ['X', 'O']:
         if flag%2==0:
             z[row][column] = 'X'
             choices[row][column] = 'X'
         else:
             z[row][column] = 'O'
             choices[row][column] = 'O'
         update_board(z)
      else:
         stdscr.addstr(24, 0, 'wrong input try again')
         stdscr.refresh()
         continue
      for n in range(0, 3):
 
           if (choices[n][0] == choices[n][1] and choices[n][n] == choices[n][2]):
               winner = True
 
           elif (choices[0][n] == choices[1][n] and choices[0][n] == choices[2][n]):
               winner = True
 
      if (choices[0][0] == choices[1][1] and choices[0][0] == choices[2][2]) or (choices[0][2] == choices[1][1] and choices[0][2] == choices[2][0]):
           winner = True
      flag = flag + 1
   if flag%2 == 0 and winner == True:
       stdscr.addstr(22,0,'Player 2 win')
       stdscr.refresh()
       stdscr.addstr(18,0,'                                    ')
       stdscr.refresh()
   elif flag%2 != 0 and winner == True:
       stdscr.addstr(22, 0, 'Player 1 win')
       stdscr.refresh()
       stdscr.addstr(20, 0, '                                    ')
       stdscr.refresh()
   if winner == False:
       stdscr.addstr(22,0,'TIE')
       stdscr.refresh()
       stdscr.addstr(20, 0, '                                    ')
       stdscr.refresh()
 
play_again = 'y'
while play_again == 'y':
   stdscr = curses.initscr()
   stdscr.addstr(0, 0,'-----------------------------------------------------------------')
   stdscr.refresh()
   stdscr.addstr(22, 0, '                         ')
   stdscr.refresh()
   z = [[0,0,0],[0,0,0],[0,0,0]]
   choices = []
   for i in range(0, 3):
       choices.append([(str(i) + '0'), (str(i) + '1'), (str(i) + '2')])
   update_board(z)
   game(z, choices)
   time.sleep(4)
   curses.endwin()
   play_again = input('Play Again (Y/N): ')
   play_again = play_again.lower()  
b = input()