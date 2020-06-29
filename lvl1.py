from __future__ import print_function
import random
 
choices = []from __future__ import print_function
import random

choices = []
print("\n**********WELCOME TO TIC TAC TOE GAME**********\n")

while 1:
    print("Choose mode of the game\n\n 1:Human Player\n 2:Computer")

    ch = int(input())

    if ch == 1:
        print("***HUMAN VS Human***\n\n")
        break
    elif ch == 2:
        print("***HUMAN VS COMPUTER***\n\n")
        break
    else:
         print("invalid choice")
 
 
for i in range(0, 3):
    choices.append([(str(i) + str(0)), (str(i) + str(1)), (str(i) + str(2))])
 
 
# print(choices)
 
def randm():
    a = random.randint(0, 2)
    b = random.randint(0, 2)
 
    return (a, b)
 
 
playerOneTurn = True
winner = False
 
 
def printBoard():
    for i in range(3):
        print(' ---------------')
        print('| ' + choices[i][0] + ' | ' + choices[i][1] + ' | ' + choices[i][2] + ' |')
 
 
flag = 0
print("*********let the game begin***********")
while not winner and flag < 9:
    printBoard()
    print("you have to entered rows sapce column\n")
    
 
    if playerOneTurn:
        print("Player 1:")
    else:
        if ch==2:
            print("Computer:")
        else:
            print("Player2")
    try:
        if playerOneTurn:
            r, c = list(map(int, input(">> ").split()))
        else:
            if ch==2:
                r, c = randm()
            else:
                r, c = list(map(int, input(">> ").split())) 
        print(" entered" + str(r) + " " + str(c))
    except:
        print("please enter a valid field")
        continue
    if choices[r][c] == 'X ' or choices[r][c] == 'O ':
        print("illegal move, plase try again")
        continue
 
    flag += 1
    if playerOneTurn:
        choices[r][c] = 'X '
    else:
        choices[r][c] = 'O '
 
    playerOneTurn = not playerOneTurn
 
    for x in range(0, 3):
 
        if (choices[x][0] == choices[x][1] and choices[x][x] == choices[x][2]):
            winner = True
 
        elif (choices[0][x] == choices[1][x] and choices[0][x] == choices[2][x]):
            winner = True
 
    if (choices[0][0] == choices[1][1] and choices[0][0] == choices[2][2]) or (
            choices[0][2] == choices[1][1] and choices[0][2] == choices[2][0]):
        winner = True
 
printBoard()
 
if winner == True:
    print("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
 
else:
    print("its a tie!")

for i in range (0, 3) :
    choices.append([(str(i) + " " +str(0)), (str(i) + " " + str(1)), (str(i) + " " + str(2))])


#print(choices)

def randm():
    
    a = random.randint(0,2)
    b = random.randint(0,2)

    return (a,b)

 
playerOneTurn = True
winner = False
 
def printBoard() :

    for i in range(3):
            print( ' -----------------')
            print( '| ' + choices[i][0] + ' | ' + choices[i][1] + ' | ' + choices[i][2] + ' |')
    print( ' -----------------')
flag = 0
while not winner and flag<9 :
    printBoard()
    print("\n\n\n")
 
    if playerOneTurn :
        print( "Player 1:")
   
   
    else :
        print( "Computer")
 
    try:
        if playerOneTurn:
            r, c = list(map(int, input(">> ").split()))
        else:
            r, c = randm()
        
        print("you entered"+str(r)+" "+str(c))
    except:
        print("please enter a valid field")
        continue
    if choices[r][c] == 'X ' or choices [r][c] == 'O ':
        print("illegal move, plase try again")
        continue
 
    flag += 1
    if playerOneTurn :
        choices[r][c] = 'X '
    else :
        choices[r][c] = 'O '

    
 
    playerOneTurn = not playerOneTurn
 
    for x in range (0, 3) :
    
        if (choices[x][0] == choices[x][1] and choices[x][x] == choices[x][2] ):
            winner = True
           
        elif (choices[0][x] == choices[1][x] and choices[0][x] == choices[2][x]) :
            winner = True
        
        
    if (choices[0][0] == choices[1][1] and choices[0][0] == choices[2][2]) or (choices[0][2] == choices[1][1] and choices[0][2] == choices[2][0]):
            winner = True



printBoard()


if winner == True: 
    print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")

else:
    print ("its a tie!")

