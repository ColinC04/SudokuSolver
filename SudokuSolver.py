##
# Program to Solve inputted Sudoku puzzle

# Used to intialize the baord
import numpy as np


# Initialize the board and open the file
board = np.empty((9,9))
with open('board.txt') as file:
    board = [[int(x) for x in line.split()] for line in file]

# Be able to output the board at the end
def output_board(bo):
    for i in range(9):
        if i%3 == 0 and i != 0:
            print("---------------------")
        
        for j in range(9):
            if j%3 == 0 and j != 0:
                print("|", end=" ")
            print(bo[i][j], end=" ")

        print(" ")

# Find the next empty spot so it can be dealt with
def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i, j)

def solve(bo):
    empty = find_empty(bo)
    if empty:
        row, col = empty
    
    else:
        return True

    # Use test values to see if it creates a valid board
    for i in range(1,10):
        if check_valid(bo,i, (row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            # Reset the value if it didn't work

            bo[row][col] = 0

    return False


def check_valid(bo, value, pos):
    # Check Row
    for i in range(9):
        if bo[pos[0]][i] == value and pos[1] !=i:
            return False

    # Check Column
    for i in range(9):
        if bo[i][pos[1]] == value and pos[0] != i:
            return False

    # Check boxes
    boxXCoordinate = pos[1]//3
    boxYCoordinate = pos[0]//3

    xIndex = boxXCoordinate*3
    yIndex = boxYCoordinate*3

    for i in range(yIndex, yIndex+3):
        for j in range(xIndex, xIndex+3):
            if bo[i][j] == value and (i,j) != pos:
                return False

    return True

solve(board)
output_board(board)

