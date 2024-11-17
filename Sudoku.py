def find_next_empty(puzzle):
    # find the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is None)

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None

def is_valid(puzzle, guess, row, col):
    # figuers out whether the guess at the row/col of the puzzle is a valid guess
    # return True if is valid, false otherwise

    # let's start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # now comes columns
    # col_vals = []
    # for r in range(0,9):
    #     col_vals += puzzle[r][col]
    col_vals = [ puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # now comes the square
    r1 = (row // 3 )*3
    c1 = (col // 3 )*3
    for r in range(r1,r1+3):
        for c in range(c1,c1+3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking technique
    # our puzzle is a list of lists, where each inner list is a row in our sudoku
    # return whether a solution exists
    # mutates puzzle to be the solution ( if solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row == None:
        return True
    
    # step 2: if there is a place to put a number, then make a guess between 1 to 9
    for guess in range(1,10):
        # step 3: check if this guess is a valid 
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place the guess
            puzzle[row][col] = guess
            # now recurse using this puzzle!
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
        # step 5: if not valid or our guess does not solve the sudoku then we nned to backtrack
        # and try a new number
        puzzle[row][col] = -1 # reset the guess
        
    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE 
    return False
if __name__ == '__main__':
    example_board = [
        [ 3, 9, -1,  -1, 5, -1,  -1, -1, -1],
        [ -1, -1, -1,  2, -1, -1,  -1, -1, 5],
        [ -1, -1, -1,  7, 1, 9,  -1, 8, -1],

        [ -1, 5, -1,  -1, 6, 8,  -1, -1, -1],
        [ 2, -1, 6,  -1, -1, 3,  -1, -1, -1],
        [ -1, -1, -1,  -1, -1, -1,  -1, -1, 4],

        [ 5, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [ 6, 7, -1,  1, -1, 5,  -1, 4, -1],
        [ 1, -1, 9,  -1, -1, -1,  2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)