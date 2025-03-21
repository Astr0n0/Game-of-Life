# Conway's Game of Life

### Overview
This is a Python implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The simulation runs in the terminal, displaying the evolution of cells over generations based on simple rules.


### Game rules
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

If you want to read more about the game, you can check [Conway's Game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).


### Features
- Randomized initial grid of live and dead cells.
- Terminal-based visualization (# for alive cells, . for dead cells).
- Calculation of the number of alive neighbors for each cell.
- Toroidal (wrap-around) grid for continuous evolution.
- Adjustable grid size and number of generations.


### Sample 
![game-of-life](https://github.com/user-attachments/assets/73608461-eca7-4722-9610-668111d6b543)


----------------------------------------------

### How to Run
1. Clone the repository:
   
   `git clone https://github.com/your-username/game-of-life.git
cd game-of-life`

2. Run the script:
   
   `python Game-of-Life.py`

3. Watch the simulation unfold in your terminal!

----------------------------------------------

### Requirements
- Python 3.x

### License
- This project is licensed under the Apache License 2.0.
