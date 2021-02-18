import random
import math

class Board:
    def __init__(self):
        self.b = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.b_og = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def printBoard(self):
        print(self.b[0][0], "|",self.b[0][1], "|", self.b[0][2])
        print("----------")

        print(self.b[1][0], "|",self.b[1][1], "|", self.b[1][2])
        print("----------")
        print(self.b[2][0], "|",self.b[2][1], "|", self.b[2][2])

    def isAvailiable(self, i, j):
        if self.b[i][j] == self.b_og[i][j]:
            return True
        else:
            return False

    def isPosAvailable(self, indexOfArray, number, human):
        if self.isAvailiable(indexOfArray, number):
            if human:
                self.b[indexOfArray][number] = 'X'
                return True
            else:
                self.b[indexOfArray][number] = 'O'
                return True
        else:
            print("This position is not available")
            print("Try Again")
            return False

    def playerMove(self, number, human):
        if number >= 0 and number < 3:
            return self.isPosAvailable(0, number, human)
        
        elif number >= 3 and number < 6:
            number -= 3
            return self.isPosAvailable(1, number, human)
        
        elif number >=6 and number <= 8:
            number -= 6
            return self.isPosAvailable(2, number, human)

class Game:
    def __init__(self):
        self.board = Board()
        self.GameOver = False
        self.HumanTurn = False

        self.makeAMove()

    def whoWon(self):
        if self.HumanTurn:
            sign = self.win_check('X', self.board.b)
            if sign == 'X':
                self.GameOver = True
                print("Human as won")
        else:
            sign = self.win_check('O', self.board.b)
            if sign == 'O':
                self.GameOver = True
                print('AI HAS WON')

    def play_Again(self):
        print("Want to play another game [y/n]")
        user_input = str(input("> ")).lower()

        if user_input == 'y':
            self.board = Board()
            self.GameOver = False
            self.HumanTurn = False
        else:
            print("Good bye")

    def win_check(self, sign, board):
        # Horizontal win check
        for i in range(3):
            if sign == board[i][0] == board[i][1] == board[i][2]:
                return sign

        # Vertical win check
        for i in range(3):
            if sign == board[0][i] == board[1][i] == board[2][i]:
                return sign

        # / diagonal win check
        if sign == board[0][0] == board[1][1] == board[2][2]:
            return sign

        # \ diagonal win check
        elif sign == board[0][2] == board[1][1] == board[2][0]:
            return sign

        return False
  
    def makeAMove(self):
        if self.GameOver:
            return
        
        if self.HumanTurn:
            isMoveSuccessful = False
            while(isMoveSuccessful == False):
                self.board.printBoard()
                print("Enter the number in the grid where you would like to place your X ")
                posPlayer = int(input("> "))
                isMoveSuccessful = self.board.playerMove(posPlayer, True)
            
            self.whoWon()
            print()
            self.HumanTurn = False

        else:
            self.make_best_move()
            print()
            self.whoWon()
            self.HumanTurn = True
            
        if self.GameOver == False:
            self.makeAMove()

    def make_best_move(self):
        i_b = None
        j_b = None
        bestScore = -math.inf
        for i in range(3):
            for j in range(3):
                #Check Spot availibilit
                if self.board.b[i][j] == self.board.b_og[i][j]:
                    #if the spot is available
                    temp = self.board.b[i][j]
                    self.board.b[i][j] = 'O'
                    #figuiring out the score
                    score = self.minimax(self.board.b, 0, False)
                    #removing the move
                    self.board.b[i][j] = temp
                    if score > bestScore:
                        bestScore = score
                        i_b = i
                        j_b = j
        self.board.b[i_b][j_b] = 'O'
        self.board.printBoard()

    def minimax(self, board, depth, isMaxing):
        if isMaxing:
            result = self.win_check('O', board)
        else:
            result = self.win_check('X', board)
        if result == 'O':
            return 10
        elif result == 'X':
            return -10

        if isMaxing == True:
            bestScore = -math.inf
            for i in range(3):
                for j in range(3):
                    if self.board.b[i][j] == self.board.b_og[i][j]:
                        # if the spot is available
                        temp = self.board.b[i][j]
                        self.board.b[i][j] = 'O'
                        # figuiring out the score
                        score = self.minimax(self.board.b, depth+1, False)
                        # removing the move
                        self.board.b[i][j] = temp
                        bestScore = max(score, bestScore)
            return bestScore

        else:
            bestScore = math.inf
            for i in range(3):
                for j in range(3):
                    if self.board.b[i][j] == self.board.b_og[i][j]:
                        # if the spot is available
                        temp = self.board.b[i][j]
                        self.board.b[i][j] = 'X'
                        # figuiring out the score
                        score = self.minimax(self.board.b, depth+1, True)
                        # removing the move
                        self.board.b[i][j] = temp
                        bestScore = min(score, bestScore)
            return bestScore
#initializse the game
Game = Game()