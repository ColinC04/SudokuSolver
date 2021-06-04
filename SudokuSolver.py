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
        for item in bo[i]:
            print(item, end=" ")

        print(" ")

# Find the next empty spot so it can be dealt with
def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i, j)

# output_board(board)

