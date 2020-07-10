'''

Information!
This code contains Level 1,2,3,4,5
Graphics part includes all the levels using Tkinter graphics
Non Graphics part lets you play on the console

'''


#Importing required modules
import math
import random
import time
import os
from tkinter import *
from tkinter import messagebox
import random as r

#declaration of dict PointTable with keys and respective values for Ai to calculate the score for each position 
PointTable = {'X  ':-1, 'O  ':1, 'tie':0}

class TicTacToe:
    '''This is a class for the game TIC-TAC-TOE. '''
    def __init__(self):
        '''The constructor for TicTacToe class:
        
        Params:
        self: instace of a class

        Attributes:
        choices: list containing choices of the board
        newboard: function containing the board of choices
        turns: integer that counts the turns
        playerturn: (bool) tells whether cross is playing
        opponent:(str) keeps record of opponent
        
        return:
        None
        '''
        self.choices=[]
        self.newBoard(self.choices)
        self.turns=0
        
        self.playerOneTurn = self.PlayerChoice()
        self.opponent = ''
        
        




    
    def newBoard(self, choices):
        '''
        Function to initialise an empty board
        
        Params:
        choices: a 2d list containing the inputs to the board
 
        Returns:
        NoneType
        '''
        choices.append(['0 0', '0 1', '0 2'])
        choices.append(['1 0', '1 1', '1 2'])
        choices.append(['2 0', '2 1', '2 2'])


    def printBoard(self, choices):
        '''
        The function to print the game board.
        
        Params:
        choices: a 2d list containing the inputs to the board
        
        Returns:
        NoneType
        '''
        print(' -----------------')
        print('| ' + choices[0][0] + ' | ' + choices[0][1] + ' | ' + choices[0][2] + ' |')
        print(' -----------------')
        print('| ' + choices[1][0] + ' | ' + choices[1][1] + ' | ' + choices[1][2] + ' |')
        print(' -----------------')
        print('| ' + choices[2][0] + ' | ' + choices[2][1] + ' | ' + choices[2][2] + ' |')
        print(' -----------------')


    def win(self, choices, turns):
        '''
        The function to check if choices are same either in each non-empty row, non-empty column or non-empty diagonal.
        
        Params:
        choices: a 2d list containing the inputs to the board
        turns: integer that counts the turns(in the words the places filled in the board by the players)
 
        
        Returns:
        String 'X  ' if X is the winner
        String 'O  ' if O is the winner
        String 'tie' if X match is draw
        None if nobody wins and turns are less than 9
        '''
        
        for x in range(0, 3):
            
            if (choices[x][0] == choices[x][1] and choices[x][0] == choices[x][2]):
                return choices[x][0]
                
     
            elif (choices[0][x] == choices[1][x] and choices[0][x] == choices[2][x]):
                return choices[0][x]
                
     
        if (choices[0][0] == choices[1][1] and choices[0][0] == choices[2][2]) or (
              choices[0][2] == choices[1][1] and choices[0][2] == choices[2][0]):
            return choices[1][1]

        if turns >= 9:
            return 'tie'  
        
        
        
        
        return None

    def randm(self):
        '''
        The function to return random integers from the given range for variables a,b.
        
        Parmas:
        self i.e. object of class TicTacToe
 
        Returns:
        a(int): random integer from the given range
        b(int): random integer from the given range
        '''
        a = random.randint(0, 2)
        b = random.randint(0, 2)

        return (a, b)
    def mode(self):
        '''
        The function to select the mode of the game.
        
        Parmas:
        self i.e. object of class TicTacToe

        Returns:
        ch(int): mode chosen from the given game modes.
        '''
        
        ch = int(input("Choose mode of the game\n\n 1:Human Player(Level 1)\n 2:AI Bot(Level 5)\n 3:Regular Bot(Level 2)\n 4:See a test run between 2 AI Bots(Level 4)\\n>>"))
        os.system("clear")
        if ch == 1:
            print("*************HUMAN VS Human***************\n\n".center(100))
            
        elif ch == 2:
            print("**************HUMAN VS AI***************\n\n".center(100))
            self.opponent = 'AI bot:'
        elif ch == 3:
            print("**************HUMAN VS Bot**************\n\n".center(100))
            self.opponent = 'bot:'
        elif ch == 4:
            print("**************Test Run*************\n\n".center(100))
            self.opponent = 'Player 2:'
        else:
            print("invalid choice")
            self.mode()
        time.sleep(0.5)
        return ch

    

    def positonCheck(self, choices, highestScore, sign1, sign2, depth, maxPlayer, alpha, beta, flag, turns):
        '''
        The function to check which position will increase chance of winning
        
        Params:
        choices: 2D list containing input to the board
        turns: integer that counts the turns
        highestScore: (int) stores the score of the position with greater chance of winning
        sign1: (str) for winning sign or ai sign(X or O)
        sign2: str for losing sign or ai sign(X or O)
        depth: int goes down for next position for a given position going further into the game 
        maxPlayer: bool gives the player for whom we want to maximise score
        alpha: int The best (highest-value) choice we have found so far at any point along the path of Maximizer
        beta: int The best (lowest-value) choice we have found so far at any point along the path of Minimizer
        flag: int keep a record whether its a maximising or minimising function
        
        Attributes:
        r(int): to traverse the rows
        c(int): to traverse the columns
        chosenposition: (tuple) gives row col position ai bot will go for
        playerOneTurn(): True if it is player1's turn
        minimax(): function that implements minimax algorithm i.e calculates scores for each position
        score: Score of a particular position i.e. chance of it being winner
 
        Returns:
        Tuple with the following elements

        highestScore: int
        chosenPosition: tuple
 
        '''
        chosenPosition = ()
        for r in range(3):
            for c in range(3):
                if  choices[r][c] != 'X  ' and  choices[r][c] != 'O  ':
                    if self.playerOneTurn:
                        choices[r][c] = sign1
                    else:
                        choices[r][c] = sign2
                    score = self.minimax(choices, depth+1, maxPlayer, turns+1, alpha, beta)
                    choices[r][c] = str(r)+" "+str(c)
                    if flag == 2:
                        if score < highestScore:
                            highestScore = score
                        beta = min(beta, highestScore)
                    else:
                        if score > highestScore:
                            highestScore = score
                            chosenPosition = (r, c)
                        if flag == 1:
                            alpha = max(alpha, highestScore)
                    if beta < alpha:
                        break
                    
        return (highestScore, chosenPosition)


    def minimax(self, choices, depth, maxPlayer, turns, alpha, beta):
        '''The function to implement the minimax algorithm.
 
        Minimax is a type of adversarial search algorithm for generating and exploring game trees.
 
        Params:
        choices: list containing choices of the board
        depth: int
        maxPlayer: bool
        turns: integer that counts the turns
        alpha: int The best (highest-value) choice we have found so far at any point along the path of Maximizer
        beta: int The best (lowest-value) choice we have found so far at any point along the path of Minimizer
        Attributes:
        win(): The function to check if choices are same either in each non-empty row, non-empty column or non-empty diagonal.
        PointTable: dict with respective keys and values.
        positionCheck(): The function to check the position of the choice and assign X or O with respective to the player's turn
 
        Returns:
        returns PointTable if there is no winner yet
        returns positionCheck if maxplayer is 1
        returns positionCheck with differrent arguments if maxplayer is 0
        '''    
        if (self.win(choices, turns) != None):
            
            return PointTable[self.win(choices, turns)]
        
        if (maxPlayer):
            return self.positonCheck(choices, -math.inf, 'X  ', 'O  ', depth, False, alpha, beta, 1, turns)[0]
         
        
        
        else:
            return self.positonCheck(choices, math.inf, 'O  ', 'X  ', depth, True, alpha, beta, 2, turns)[0]










    def PlayerChoice(self):
        '''The function to determine the first player randomly.
 
        Attributes:
        random(module): random variable generators
        
        Returns:
        True if player1 goes first with X
        False if player2 goes first with O.
        '''

        if(bool(random.getrandbits(1))):
            
           
            return True
        
        return False

    def move(self, r, c):
        '''
        The function that assigns X or O to the choice, according to the player's turn and shifts the turn to the next player.
 
        Params:
        r(int): integer in the given range
        c(int): integer in the given range
 
        Attributes:
        choices: list containing choices of the board
        turns: integer that counts the turns
        playerOneTurn(bool): True if it is player1's turn
 
        Returns:
        returns nothing.
        '''
        self.turns += 1
        if self.playerOneTurn:
            self.choices[r][c] = 'X  '
        else:
            self.choices[r][c] = 'O  '
        self.playerOneTurn = not self.playerOneTurn
    def declareWin(self):
        '''
        The function to declare the winner.
        
        Attributes:
        opponent: str
        win(): The function to check if choices are same either in each non-empty row, non-empty column or non-empty diagonal.
 
        Returns:
        NoneType
        '''
        print({'O  ':self.opponent+" wins!", 'X  ':'Player 1 wins!', 'tie':"Its a Tie!"}[self.win(self.choices,self.turns)])
     

    
    def game(self):
        '''The function to initialise the TIC-TAC-TOE Game.
 
        Attributes:
        ch(int): mode chosen from the given game modes.
        choices: list containing choices of the board.
        mode(): The function to select the mode of the game.
        playerOneTurn(bool): True if it is player1's turn.
        win(): The function to check if choices are same either in each non-empty row, column or diagonal.
        printBoard(): The function to print the game board.
        PointTable: dict with keys and respective values.
        PlayerChoice(): The function to determine the first player randomly.
        opponent: str
        positionCheck(): The function to check the position of the choice and assign X or O with respective to the player's turn.
        move(): The function that assigns X or O to the choice according to the player's turn and shifts the turn to the next player.
        declareWin(): The function to declare the winner.
        restart: str
 
        Returns:
        NoneType
        '''
    
        os.system('clear')
        print("\n**********WELCOME TO TIC TAC TOE GAME**********\n")


        self.ch = self.mode()
        os.system('clear')
        print("*********Toss*************".center(100))
        
        if self.playerOneTurn:
                print("PlayerOne goes first with X".center(100))
        else:
                print("Player2 goes first with O".center(100))
        
    
        print("*********let the game begin***********".center(100))
        time.sleep(1)

    
        #size = int(input("size of the board"))

        while self.win(self.choices, self.turns) == None:
            os.system('clear')
            self.printBoard(self.choices)
            
            global PointTable
            if self.playerOneTurn:
                print("Player 1:")
            else:
                if self.ch == 2:
                    
                    print("AI bot:")
                elif self.ch == 1 or self.ch == 4:
                
                    print("Player2")
                elif self.ch == 3:
            
                    print("Bot")
            
            try:
                if self.playerOneTurn:
                
                    if self.ch == 4:
                        PointTable = {'X  ':1, 'O  ':-1, 'tie':0}                       
                        r, c = self.positonCheck(self.choices, -math.inf, 'X  ', 'O  ', 0, False, -math.inf, math.inf, 0, self.turns)[1]
                    else:
                        r, c = list(map(int, input("Enter row and column separated by spaces\n >> ").split()))
                else:
                    if self.ch == 2 or self.ch == 4:
                        PointTable = {'X  ':-1, 'O  ':1, 'tie':0}
                        r, c = self.positonCheck(self.choices, -math.inf, 'X  ', 'O  ', 0, False, -math.inf, math.inf, 0, self.turns)[1]
                    elif self.ch == 1:
                        r, c = list(map(int, input(">> ").split()))
                    else:
                        while 1:
                            r, c = self.randm()
                            if not (self.choices[r][c] == 'X  ' or self.choices[r][c] == 'O  '):
                                break
                print("entered\n" + str(r) + " " + str(c))
                time.sleep(0.5)
                if self.choices[r][c] == 'X  ' or self.choices[r][c] == 'O  ':
                    print("illegal move, plase try again")
                    continue

            except:
                print("please enter a valid field")
                time.sleep(1)
                continue
            
            
            
            self.move(r,c)



        os.system('clear')
        self.printBoard(self.choices)
  
        self.declareWin()

       




class GUI(TicTacToe):
    '''
    Uses Tkinter to form a tictactoe game
    '''
    def __init__(self):
        '''
        Constructor
        Initialises the game windows
        '''
        self.board = TicTacToe()
        self.mode()

        self.game()
        self.change_a()
    
    
    def game(self):
        '''
        Initialises game Board for TicTacToe

        Params:
        self: Instance of a class

        Return:
        NoneType

        '''
        self.app = Tk()
        self.app.title('TicTacToe')
        self.app.resizable(width=True, height=True)
        self.colour={'O':"maroon",'X':"black"}
        
        #setting board buttons
        self.b=[[],[],[]]
        for i in range(3):
                for j in range(3):
                        self.b[i].append(self.button(self.app))
                        self.b[i][j].config(command= lambda row=i,col=j:self.click(row, col))
                        self.b[i][j].grid(row=i,column=j)
        
        self.reseter()
        
        
        #Setting reset button
        handler = lambda : self.reset()
        button = Button(self.app, width=10, text='reset', bd=5, command=handler, font=('arial',18,'bold'))
        button.grid(row=4, column=0, columnspan=3)

    def mode(self):
        '''
        To set mode of the game by giving a choice for opponents

        Params:
        self: Instance of a class

        Return
        None
        '''
        self.root = Tk()
        self.root.title("MODE OPTIONS")
        canvas = Canvas(self.root, height=300,width=400)
        canvas.pack()
        frame = Frame(self.root, bg='purple')
        frame.place(relx = 0, rely = 0, relwidth=1, relheight = 1)
        
        label = Label(frame,text = "Choose your opponent", font=('arial',20,'bold'),bg = 'pink', fg = 'maroon')
        label.place(relx=0.16,rely = 0)
       
        #Setting mode buttons
        self.mb = ['','','','']
        self.mb[0]= Button (frame, text="Human", relief=RAISED, font=('arial',15,'bold'), bd = 4 )
        self.mb[0].config(command= lambda i=0:self.menu_click(i))
        self.mb[0].place(relx=0.34,rely =0.2)
        self.mb[1]=Button (frame, text="AI", relief=RAISED, font=('arial',15,'bold'), bd = 4 )
        self.mb[1].config(command= lambda i=1:self.menu_click(i))
        self.mb[1].place(relx=0.38,rely = 0.4)
        self.mb[2]=Button (frame, text="Bot", relief=RAISED, font=('arial',15,'bold'), bd = 4 )
        self.mb[2].config(command= lambda i=2:self.menu_click(i))
        self.mb[2].place(relx=0.37,rely = 0.6)
        self.mb[3]=Button (frame, text="Test Run", relief=RAISED, font=('arial',15,'bold'), bd = 4 )
        self.mb[3].config(command= lambda i=3:self.menu_click(i))
        self.mb[3].place(relx=0.32,rely = 0.8)
        self.root.mainloop()
            


    def menu_click(self,i):
        '''
        Function tells what is to be done once a mode is selected

        Params:
        self: Instance of the class
        i: index of the chosen mode button

        Return:
        None
        '''
        self.mb[i].config(state=DISABLED, relief = "sunken")
        self.board.opponent = self.mb[i]["text"]
        messagebox.showinfo("Opponent", self.board.opponent+" with 'O'")
        self.root.destroy()
        
        

    def button(self,frame):
        '''
        Sets the button structure 

        Params:
        self: Instance of the class
        frame: the window where button would be placed

        Return:
         b: i.e. the button on the tictactoe board

        '''          
        b=Button(frame,bg="papaya whip",width=3,text="   ",font=('arial',60,'bold'),bd=10)
        return b


    def change_a(self): 
        '''
        Determines position for the bots to play

        Params:
        self: Instance of the class
        frame: the window where button would be placed

        Return:
        None
        '''
        global PointTable           
        if self.board.playerOneTurn == True:
            self.a = 'X'
            self.label.config(text=self.a+"'s Chance")
            if self.board.opponent == "Test Run":
                
                self.app.config(cursor="watch")
                
                PointTable = {'X  ':1, 'O  ':-1, 'tie':0}
                r,c = self.board.positonCheck(self.board.choices,-math.inf, 'X  ', 'O  ', 0, False, -math.inf, math.inf, 0, self.board.turns)[1]
                
                self.click(r,c)
        else:
            self.a = 'O'
            self.label.config(text=self.a+"'s Chance")
            if(self.board.opponent != "Human"):
                
                self.app.config(cursor="watch")
                if(self.board.opponent == "Bot"):
                    while 1:
                        r, c = self.board.randm()
                        if not (self.board.choices[r][c] == 'X  ' or self.board.choices[r][c] == 'O  '):
                            break
                elif(self.board.opponent == "AI" or self.board.opponent == "Test Run"):
                    
                    PointTable = {'X  ':-1, 'O  ':1, 'tie':0}
                    r,c = self.board.positonCheck(self.board.choices,-math.inf, 'X  ', 'O  ', 0, False, -math.inf, math.inf, 0, self.board.turns)[1]
                
                self.click(r,c)

        

    def reseter(self): 
        '''
        Sets the initial condition reset the game

        Params:
        self: Instance of the class
        frame: the window where button would be placed

        Return:
        None
        '''
        if self.board.playerOneTurn == True:
            self.a = 'X'
            messagebox.showinfo("Toss","Player 1 goes first with X")
        else:
            self.a = 'O'
            messagebox.showinfo("Toss", "Opponent goes first with O")
        self.label=Label(text=self.a+"'s Chance",font=('arial',20,'bold'))
        self.label.grid(row=3,column=0,columnspan=3)

     
    def reset(self):
        '''
        Function runs when the reset button is pressed

        Params:
        self: Instance of the class

        Return:
        None
        '''
        self.app.destroy()
        GUI()

    
    
    
    def check(self):
        '''
        To check whether match has ended and declare winner

        Params:
        self: Instance of the class


        Return:
        None
        '''
        if self.board.win(self.board.choices,self.board.turns)!=None:
            messagebox.showinfo("Result",{'O  ':self.board.opponent+" wins!", 'X  ':'Player 1 wins!', 'tie':"Its a Tie!"}[self.board.win(self.board.choices,self.board.turns)] )
            self.label.config(text="Match ended")

        else:
            self.change_a()
            
            
            
    

    def click(self,row,col):
        '''
        Runs an infinite loop mainloop() used to run the application, wait for an event to occur and process the event as long as the window is not closed.

        Params:
        self: Instance of the class
        row: int row on the board
        col: int column on the board

        Returns:
        None

        '''
        
        self.board.move(row, col)
        self.b[row][col].config(text=self.board.choices[row][col],state=DISABLED,disabledforeground=self.colour[self.a], relief = "sunken")
        self.check()
        self.app.config(cursor="")
        
        
   
     
    def mainloop(self):
        '''
        Runs an infinite loop mainloop() used to run the application, wait for an event to occur and process the event as long as the window is not closed.

        Params:
        self: Instance of the class

        Returns:
        None
        '''
        self.app.mainloop()
     
print("\n*********************************************************\nInstructions!!!\nThis code contains Level 1,2,3,4,5\nGraphics part includes all the levels using Tkinter graphics\nNon Graphics part lets you play on the console\n***********************************************************")
    
while 1:
    try:
        graphics = int(input("\n1: With graphics(Tkinter Graphics Level 3)\n2: Without Graphics(On Console)\nChoose>>"))
    
        if graphics == 2:
            new_game = TicTacToe()
            new_game.game()
        elif graphics ==1:
            GUI().mainloop()
        else:
            print("Wrong input!")
            continue
    except:
        print("Wrong input!\ntry again!")
        continue


    restart = input("Do you want to play agin?\nIf not press n to exit!")
    restart.lower()
    
    if restart == 'n':
        break


