# Sudoku Solver (CSP-based Backtracking)
## Sean Hulseman, CS131, November 2024
This project is a Sudoku solver that uses a backtracking algorithm to solve Sudoku puzzles. The solver implements constraint satisfaction problem (CSP) principles, ensuring that the puzzle adheres to the fundamental rules of Sudoku, such as:

- Each row must contain the digits 1 through 9 without repetition.
- Each column must contain the digits 1 through 9 without repetition.
- Each 3x3 subgrid must contain the digits 1 through 9 without repetition.

The solver uses recursive backtracking, which tries numbers 1-9 in empty cells and backtracks when it encounters a conflict.

## Prerequisites

This program is written in Python 3, so you'll need Python installed on your system. It doesn't require any additional packages or libraries, making it easy to run directly.

### Steps to Run the Code:

1. **Download the ZIP file** containing the project.
2. **Extract the ZIP file** to a folder on your computer.
3. **Navigate to the project folder** and locate the Python script (e.g., `sudoku_solver.py`).
4. **Run the Python script**:
   - Open a terminal or command prompt.
   - Navigate to the folder where the Python script is located.
   - Run the following command:
     ```bash
     python sudoku_solver.py
     ```
   - The script will prompt you to choose one of the predefined Sudoku puzzles to solve. With additional time, more difficult sudoku puzzles can be tested along with more advanced algorithms.

## Sudoku Solver Overview

This solver uses **Backtracking** and **Constraint Satisfaction Problem (CSP)** techniques to solve the Sudoku puzzle. Here's a brief explanation of how the problem is set up and solved:

### CSP Setup

1. **Variables**: The variables in the Sudoku grid are the empty cells (denoted by 0). Each variable represents a cell in the grid, and its domain consists of the numbers 1 to 9.

2. **Constraints**:
   - **Row Constraint**: Each number 1 through 9 must appear exactly once in each row.
   - **Column Constraint**: Each number 1 through 9 must appear exactly once in each column.
   - **Subgrid Constraint**: Each number 1 through 9 must appear exactly once in each of the nine 3x3 subgrids.

3. **Domains**: For each empty cell (0), its domain is initially all numbers 1 through 9. The backtracking algorithm will try placing different numbers in the empty cells, checking if they violate the constraints.

### Solving the Puzzle

1. **Find an empty location**: The algorithm begins by identifying an empty cell in the grid.
2. **Try each number**: For each empty cell, the solver tries placing the numbers 1-9. It checks if placing a number violates any of the Sudoku constraints (row, column, or subgrid).
3. **Check for validity**: If the number is valid (doesn't violate constraints), it is placed tentatively in the cell.
4. **Recursion**: After placing a number, the solver recursively tries to solve the rest of the grid. If it encounters a conflict later, it backtracks by removing the number and trying the next one.
5. **Backtrack**: If no valid number can be placed in a given empty cell, the algorithm backtracks to the previous cell, changes its number, and continues from there.
6. **Completion**: The algorithm finishes when all cells are filled without any conflicts, or it determines that no solution exists.

The program automatically selects one of the two predefined puzzles (grid1 or grid2) to solve. If the puzzle is solvable, the script will print the solved grid. If no solution exists, it will indicate that the puzzle is unsolvable.

## Sample Usage

### Sample Puzzle 1:

```
6 . 8 | 7 . 2 | 1 . .
4 . . | . 1 . | . . 2
. 2 5 | 4 . . | . . .
-----------------------
7 . 1 | . 8 . | 4 . 5
. 8 . | . . . | . 7 .
5 . 9 | . 6 . | 3 . 1
-----------------------
. . . | . . 6 | 7 5 .
2 . . | . 9 . | . . 8
. . 6 | 8 . 5 | 2 . 3
```

### Solved Puzzle 1:

```
6 1 8 | 7 5 2 | 1 9 4
4 9 3 | 6 1 7 | 8 4 2
9 2 5 | 4 3 8 | 6 1 7
-----------------------
7 3 1 | 2 8 4 | 4 6 5
1 8 7 | 5 2 9 | 3 7 4
5 4 9 | 3 6 4 | 3 8 1
-----------------------
8 1 4 | 5 7 6 | 7 5 6
2 6 3 | 5 9 1 | 5 2 8
3 7 6 | 8 4 5 | 9 1 3
```

## Algorithm Explanation

The solver uses **Backtracking** combined with a simple **constraint check** to solve the puzzle. Here's how the algorithm works:

1. **Backtracking**: This is a recursive algorithm that builds solutions incrementally by making choices. It tries a number in an empty cell and proceeds with the next empty cell. If it encounters a conflict (i.e., a number violates Sudoku constraints), it backtracks and tries a different number.
   
2. **Constraint Validation**: Before placing a number, the algorithm checks:
   - **Row Constraint**: The number must not appear in the same row.
   - **Column Constraint**: The number must not appear in the same column.
   - **Subgrid Constraint**: The number must not appear in the same 3x3 subgrid.
   
3. **Termination**: The algorithm terminates when all empty cells have been filled with valid numbers or when no solution is found.


