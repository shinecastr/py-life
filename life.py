import numpy as np
from copy import copy
from time import sleep
import curses
from curses import wrapper

curses.initscr()
curses.curs_set(False)
a = [-1, 0, 1]
rows = curses.LINES
cols = curses.COLS
board = np.zeros((rows, cols))
swap = copy(board) #make two 2d arrays the size of the terminal window


def step(): #stores the next generation into the swap array and writes into the board
    for i  in range(rows):
        for j in range(cols): #iterate over the indecies of the 2D array
            #rules of the game go here!
            #if a living cell has 2 or 3 neighbors it stays alive
            #otherwise, a living cell will die
            #a dead cell with three neighbors will be alive
            #all others will remain dead
            if(board[i][j] == 1):
                if(getNeighbors(i, j) == 2 or getNeighbors(i, j) == 3):
                    swap[i][j] = 1
                else:
                    swap[i][j] = 0
            elif getNeighbors(i, j) == 3:
                swap[i][j] = 1
            else:
                swap[i][j] = 0

    for i in range(rows):
        for j in range(cols):
            board[i][j] = swap[i][j]

def getNeighbors(row, col): #returns how many neighboring cells are alive
    n_neighbors = 0
    for i in a:
        for j in a: #this sets i and j to every combination of + and -1 to check all surrounding cells
            if(row + i in range(rows) and col + j in range(cols) and not (i == 0 and j == 0)):
            #this disgusting if statement excludes the cell itself and cells outside the array from being indexed
                n_neighbors+=board[row+i][col+j]
    return n_neighbors

def main(stdscr):
    stdscr.clear()
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                stdscr.addstr(i, j, "#")

    stdscr.refresh()
    sleep(0.1)
    step()
#set living cells here

board[0][2] = 1
board[1][0] = 1
board[1][2] = 1
board[2][1] = 1
board[2][2] = 1

while 1:
    wrapper(main)
