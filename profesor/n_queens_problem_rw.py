#------------------------------------------------------------------------------------------------------------------
#   Random walk algorithm for the n-queen problem
#
#   Modified by Dr. Santiago Enrique Conant Pablos
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------
import time
import random
import math

#------------------------------------------------------------------------------------------------------------------
#   Class definitions
#------------------------------------------------------------------------------------------------------------------

class Board(object):
    """ Class that represents n-queens placed on a chess board. Each queen is located in a 
        different column. The board is represented by a list of n rows. """
    
    def __init__(self, n, randomize = True):        
        """ 
            This constructor initializes the board with n queens. 

            n: The number of rows and columns of the chess.
            randomize: True indicates that the initial queen rows are choosen randomly.
                       False indicates that the queens are placed on the first row.
        """
        self.n = n
        self.queens = []
        
        for col in range(n):
            if randomize:
                row = random.choice(range(n))
            else: # Place the queens on the first row
                row = 0
            self.queens.append(row)

    def show(self):        
        """ This method prints the current board. """                
        for row in range(self.n):
            for col in range(self.n):
                if self.queens[col] == row:
                    print (' Q ', end = '')
                else:
                    print (' - ', end = '')
            print('')
        print('')
    
    def cost(self):
        """ This method calculates the cost of this solution (the number of queens that are not safe). """
        c = 0
        for i in range(self.n-1):
            queen = self.queens[i]
            safe = True
            for j in range(i+1, self.n):
                other_queen = self.queens[j]
                if (queen == other_queen):
                    # The queens are on the same row
                    safe = False
                elif abs(queen-other_queen) == abs(i-j):
                    # The queens are on the same diagonal
                    safe = False
            if not safe:
                c += 1
        return c

    def neighbor(self):
        """ This method returns a board instance like this one but with one random move made. """        
        
        # Copy current board
        new_board = Board(self.n, False)
        for i in range(self.n):
            new_board.queens[i] = self.queens[i]
             
        # Select one random queen and a new random row
        queen = random.choice(range(self.n))
        valid_position = False
        while not valid_position:            
            new_row = random.choice(range(self.n))
            if self.queens[queen] != new_row:
                valid_position = True
        
        # Update one queen selected randomly
        new_board.queens[queen] = new_row

        return new_board
    
                                       
#------------------------------------------------------------------------------------------------------------------
#   Random Walk Algorithm
#------------------------------------------------------------------------------------------------------------------
def random_walk(current, max_steps):
    print("-------- Initial state -----------")
    current.show()
    cost = current.cost()       # Initial cost   
    print("Initial Cost: ", cost) 

    step = 0;                   # Step count
    while (step < max_steps) and (cost > 0):
        step += 1        
        
        # Get a random neighbor
        current = current.neighbor()
        cost = current.cost()

        print("Iteration: ", step, "    Cost: ", cost)

    print("--------Solution-----------")
    current.show()
    print("Final Cost: ", cost)
    return current

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------
random.seed(time.time()*1000)
initial_board = Board(8, True)      # Initialize board
max_steps = 100000                  # Maximum number of steps
solution = random_walk(initial_board, max_steps)

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------