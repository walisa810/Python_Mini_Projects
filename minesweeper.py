import random
import re
# let's create a board object to represent the minesweeper game
# this is sothat we can just just say "create a board",or
# "dig here",or "render this game" for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # let's keep track of these parameters. they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function!
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row,col) tuples into this set 
        self.dug = set() # if we dig 0,0 then self.dug = {(0,0)}

    def make_new_board(self):

        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here

        board = [ [None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        #[[ None, None, ..., None],
        # [None, None, ..., None],
        # [ None, None, ..., None],
        # [ None, None, ..., None]]

        bomb_planted = 0
        while bomb_planted < self.num_bombs:
            loc = random.randint(0,self.dim_size**2 -1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*': # already a bomb
                continue
            board[row][col] = '*' # plant the bomb
            bomb_planted += 1
        return board
   
    def assign_values_to_board(self):
        # now let's assign (0-8) values for empty cells which represents
        # how many neighbouring bombs there are. we can precompute these
        # and it'll save us some effort checking what's around the board
        # later on.

        for r in range(0,self.dim_size):
            for c in range(0,self.dim_size):
                if self.board[r][c] == None or self.board[r][c] == ' ':
                    count = 0
                    if r > 0 and c > 0 and self.board[r-1][c-1] =='*':
                        count += 1
                    if r > 0 and self.board[r-1][c] =='*':
                        count += 1
                    if r > 0 and c < self.dim_size-1 and self.board[r-1][c+1] =='*':
                        count += 1
                    if r < self.dim_size-1 and self.board[r+1][c] =='*':
                        count += 1
                    if r < self.dim_size-1 and c > 0 and self.board[r+1][c-1] =='*':
                        count += 1
                    if r < self.dim_size-1 and c < self.dim_size-1 and self.board[r+1][c+1] =='*':
                        count += 1
                    if c < self.dim_size-1 and self.board[r][c+1] == '*':
                        count += 1
                    if c > 0 and self.board[r][c-1] == '*':
                        count += 1
                    self.board[r][c] = count
                    
    def dig(self, row, col ):
        # dig at that location!
        # return True if successful dig, False if bomb dug

        # a few scenarios:
        # hit a bomb --> game over
        # dig at a location with neighbouring bombs --> finish dig
        # dig at location with no neighbouring bombs --> recursively dig neighbours!

        self.dug.add((row, col)) # keep track that we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col] == 0:
        for r in range( max(0,row-1),min(self.dim_size-1,row+1)+1):
            for c in range( max(0,col-1),min(self.dim_size-1,col+1)+1):
                if (r,c) in self.dug:
                    continue
                self.dig(r, c) 
        return True

    def printg(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        visible_board = [ [None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        for row in range(self.dim_size):
            x = []
            for col in range(self.dim_size):
                x += visible_board[row][col]
            print('| '+' | '.join(x)+' |')
        
# play the game
def play( dim_size = 10, num_bombs = 10):
    # step 1: create the board and plant the bombs
    board = Board( dim_size, num_bombs )
    # step 2: show the user the board and ask for where they want to dig
    # step 3a: if location is a bomb, show game over message
    # step 3b: if location is not a bomb, dig recursively until each square
    #           is at least next to a bomb
    # step 4: repeat steps 2 and 3a/b untilthere are nomotre places to dig--> VICTORY!
    safe = True

    while len(board.dug) < dim_size ** 2 - num_bombs:
        board.printg()
        user_input = re.split(',(\\s)*',input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= dim_size or col < 0 or col >= dim_size :
            print("Invalid input. Try Again")
            continue
        safe = board.dig(row, col)

        if not safe:
            # dug a bomb
            break
    if safe:
        print("Congratulations! You won")
    else:
        print("Sorry!! GAME OVER")
        board.dug = [(r,c) for r in range(dim_size) for c in range(dim_size)]
        board.printg()

if __name__ == "__main__":
    play()
