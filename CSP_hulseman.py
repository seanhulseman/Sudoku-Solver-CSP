# CSP Sudoku Solver. Sean Hulseman.
def print_grid(grid):
    """Print the Sudoku grid."""
    for row in grid:
        print(" ".join(str(val) if val != 0 else "." for val in row))
    print()

def is_valid(grid, row, col, num):
    """Check if placing `num` at grid[row][col] is valid according to Sudoku rules."""
    # Check row, column, and 3x3 subgrid
    if num in grid[row]:
        return False
    if num in (grid[r][col] for r in range(9)):
        return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False
    return True

def find_empty_location(grid):
    """Find the next empty cell in the grid (marked as 0)."""
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return (r, c)
    return None

def solve(grid):
    """Solve the Sudoku grid using backtracking."""
    empty_loc = find_empty_location(grid)
    if not empty_loc:
        return True  # Puzzle solved if no empty cells remain
    
    row, col = empty_loc
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num  # Assign the number tentatively
            
            if solve(grid):  # Recursively attempt to solve
                return True
            
            grid[row][col] = 0  # Backtrack if not valid
    
    return False  # Trigger backtracking if no numbers are valid

def get_user_input():
    """Prompt the user to input a custom Sudoku grid."""
    print("Enter your Sudoku grid row by row (use 0 for empty cells):")
    grid = []
    for i in range(9):
        row = input(f"Enter row {i+1}: ")
        # Ensure the row is a valid Sudoku row
        grid.append([int(x) for x in row.split()])
    return grid

def main():
    # Predefined grids
    grid1 = [
        [6, 0, 8, 7, 0, 2, 1, 0, 0],
        [4, 0, 0, 0, 1, 0, 0, 0, 2],
        [0, 2, 5, 4, 0, 0, 0, 0, 0],
        [7, 0, 1, 0, 8, 0, 4, 0, 5],
        [0, 8, 0, 0, 0, 0, 0, 7, 0],
        [5, 0, 9, 0, 6, 0, 3, 0, 1],
        [0, 0, 0, 0, 0, 6, 7, 5, 0],
        [2, 0, 0, 0, 9, 0, 0, 0, 8],
        [0, 0, 6, 8, 0, 5, 2, 0, 3]
    ]
    grid2 = [
        [0, 7, 0, 0, 4, 2, 0, 0, 0], 
        [0, 0, 0, 0, 0, 8, 6, 1, 0], 
        [3, 9, 0, 0, 0, 0, 0, 0, 7], 
        [0, 0, 0, 0, 0, 4, 0, 0, 9], 
        [0, 0, 3, 0, 0, 0, 7, 0, 0], 
        [5, 0, 0, 1, 0, 0, 0, 0, 0], 
        [8, 0, 0, 0, 0, 0, 0, 7, 6], 
        [0, 5, 4, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 1, 0, 0, 5, 0]
    ]
    
    # Ask the user to choose a grid
    # Another version of this asked the user if they want to build type a puzzle in but that was cumbersome
    print("Choose a Sudoku grid:")
    print("1. Sample Puzzle 1")
    print("2. Sample Puzzle 2")

    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        sudoku_grid = grid1
    elif choice == "2":
        sudoku_grid = grid2
    else:
        print("Invalid choice. Using Sample Puzzle 1 by default.")
        sudoku_grid = grid1
    
    print("\nInitial Sudoku Grid:")
    print_grid(sudoku_grid)

    if solve(sudoku_grid):
        print("Solved Sudoku Grid:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
