# Validating the input
def validateInput(i):
    try:
        row = [int(i) for i in input(f'Enter the value of row {i+1}: ')]
        if len(row)<9:
            print('-\"All values are not entered, try again\"')
            return validateInput(i)
        elif len(row)>9:
            print('-\"Extra values are entered, try again\"')
            return validateInput(i)
    except:
        print('-\"Enter only numbers, try again\"')
        return validateInput(i)
    return row

# Prints the sudoku board
def printBoard(sudoku):
    print(' ' + '-'*29)
    for i in range(9):
        print('|', end='')
        for j in range(9):
            val = sudoku[i][j]
            if val==0:
                print('   ', end='')
            else:
                print(' ' + str(val) + ' ', end='')
            if (j+1)%3==0:
                print('|', end='')
        print()
        if i!=8 and (i+1)%3==0:
            print('|' + '-'*9 + '|' + '-'*9 + '|' + '-'*9 + '|')
    print(' ' + '-'*29)

# Checks that the row, column, box does not contain the numbner n
def isValidMove(sudoku, x, y, n):
    # Checking in row
    for i in range(9):
        if sudoku[x][i]==n:
            return False
    # Checking in column
    for i in range(9):
        if sudoku[i][y]==n:
            return False
    # Checking in box
    boxX = (x//3)*3
    boxY = (y//3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[boxX+i][boxY+j]==n:
                return False
    return True

# Solves the sudoku
def solveSudoku(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                for n in range(1, 10):
                    if isValidMove(sudoku, i, j, n):
                        sudoku[i][j]=n
                        if solveSudoku(sudoku):
                            return True
                        sudoku[i][j]=0
                return False
    return True

# Program starts here..........................................................................................................

sudoku = []
# Example Sudoku board (0 represents empty cells)
'''sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]'''

# Takes input only when the sudoku list is empty
if len(sudoku)==0:
    print('.......................................')
    print('Note - Enter 0 in place of blank Spaces')
    print('Example - 000000000')
    print('.......................................')

    for i in range(9):
        row = validateInput(i)
        sudoku.append(row)

# Prints the given sudoku question
print()
print('Question Sudoku')
printBoard(sudoku)

if solveSudoku(sudoku):
    # Prints the solution of sudoku
    print()
    print('Sudoku Solution')
    printBoard(sudoku)
else:
    print("No solution exists.")