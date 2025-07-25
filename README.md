# Sudoku-Bruteforcer

This is a simple Sudoku solver that uses a backtracking algorithm to find a solution to a given Sudoku puzzle.

## How to use

1.  Run the `main.py` file.
2.  You will be prompted to enter the values for each cell of the Sudoku grid.
3.  Enter a number between 1 and 9 for a filled cell, and 0 or Enter for an empty cell.
4.  Once you have entered all the values, the solver will attempt to find a solution.
5.  You can choose to run the solver in "Speed Mode" or not. In "Speed Mode", the board is not displayed at each step of the resolution, which makes it faster.

## Files

*   `main.py`: The main file of the project. It contains the logic for the Sudoku solver.
*   `show.py`: This file contains the function to display the Sudoku board.
*   `.gitignore`: This file is used to ignore the `__pycache__` folder.

## How it works

The solver uses a backtracking algorithm to find a solution. The `isValid` function checks if a given number can be placed in a given cell. The `resolve` function uses recursion to try all possible combinations of numbers until a solution is found.