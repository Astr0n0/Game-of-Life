import random
import time
import os

def clear_screen():
    # to clear the screen in Windows and Linux
    if os.name == 'nt':  # for windows
        os.system('cls')
    else:  # for Linux and Mac
        print('\033[H\033[J', end='')

def create_initial_grid(rows, cols):
    # generating a random grid of alive and dead cells
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    # displaying the grid in the terminal
    for row in grid: # '.' for dead cells and '#' for alive ones 
        print(''.join('⬜' if cell == 1 else '⬛' for cell in row))

def get_neighbors(grid, row, col, rows, cols):
    # the number of alive neighbors of a cell
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            r = (row + i) % rows  # making the grid toroidal
            c = (col + j) % cols
            count += grid[r][c]
    return count

def next_generation(grid, rows, cols):
    # game rules
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(grid, i, j, rows, cols)
            if grid[i][j] == 1:  # alive cells
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0  # death
                else:
                    new_grid[i][j] = 1  # survive
            else:  # dead cells
                if neighbors == 3:
                    new_grid[i][j] = 1  # birth
                else:
                    new_grid[i][j] = 0
    
    return new_grid

def main():
    # initial setup
    rows, cols = 30, 40  # grid size
    grid = create_initial_grid(rows, cols)
    generation = 0

    try:
        while True:
            clear_screen()
            print(f"     Generation < {generation} > \n")
            print_grid(grid)
            grid = next_generation(grid, rows, cols)
            generation += 1
            time.sleep(0.05)
    
    except KeyboardInterrupt:
        if generation == 1:
            print("\n The Game stopped at the First generation.")
        elif generation == 2:
            print("\n The Game stopped at the Second generation.")
        elif generation == 3:
            print("\n The Game stopped at the Third generation.")
        else:
            print("\n The Game stopped at the", f"{generation}th", "generation.")

if __name__ == "__main__":
    main() 