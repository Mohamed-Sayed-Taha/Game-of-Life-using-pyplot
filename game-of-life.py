"""
Conway's Game of Life
==============================
A cellular automaton devised by mathematician John Conway.
Zero-player game where evolution is determined by initial state.

Rules:
1. Any live cell with <2 live neighbors dies (underpopulation)
2. Any live cell with 2-3 live neighbors lives (survival)
3. Any live cell with >3 live neighbors dies (overpopulation)
4. Any dead cell with exactly 3 live neighbors becomes alive (reproduction)
"""

import matplotlib.pyplot as plt
import numpy as np

class GameOfLife():
    """
    A class representing Conway's Game of Life simulation.
    
    Attributes:
    -----------
    cols : int --> Number of columns in the grid (width)
    rows : int --> Number of rows in the grid (height)
    life_grid : numpy.ndarray --> 2D array where 0 = dead cell, 1 = live cell
    
    Methods:
    --------
    get_grid() -> numpy.ndarray -->Returns current grid state
    print_grid() -> None -->Prints grid to console
    populate_grid(coords: list of tuples) -> None --> specified cells to live state
    make_step() -> None --> Advances simulation by one generation
    make_n_steps(n: int) -> None --> Advances simulation by n generations
    draw_grid() -> None --> Visualizes current grid using matplotlib
    """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.life_grid = np.zeros(shape=(rows, cols), dtype= int)
        self.current_step = 0
        self.fig = None  # Store figure
        self.ax = None   # Store axis
        self.im = None   # Store image object

    def randomize(self, density=0.3):
        """Fill grid with random live cells"""
        self.life_grid = np.random.choice([0, 1], 
                                     size=(self.rows, self.cols), 
                                     p=[1-density, density])
        self.current_step = 0

    def get_grid(self) -> np.ndarray:
        return self.life_grid

    def print_grid(self):
        print(self.life_grid)

    def populate_grid(self, coords):
        """
        Set specific cells to live state.
        
        Parameters:
        -----------
        coords : list of tuples --> List of (row, column) coordinates to set as live cells
            
        Note:
        Coordinates are (row, column) format, both starting from 0 to max number of columns or rows
        """
        for r,c in coords:
            if 0 <= r < self.rows and 0 <= c < self.cols:
                self.life_grid[r][c] = 1
        self.current_step = 0   

    def make_step(self):
        """
        Advance the simulation by one generation.
        
        Applies Conway's four rules simultaneously to all cells:
        - Live cells with 2-3 neighbors survive
        - Live cells with 0-1 or 4+ neighbors die
        - Dead cells with exactly 3 neighbors become alive
        
        The entire grid updates at once (synchronous update).
        """
        # Count Neighbors
        g = self.life_grid
        cols, rows= self.cols, self.rows 
        self.current_step += 1
        neighbors = {}
        for rc in range(rows):
            for cc in range(cols):
                sum_neighbors = 0
                for r in [-1 , 0, 1]:
                    for c in [-1, 0, 1]:
                        if r == 0 and c == 0:
                            continue
                        rn = rc + r
                        cn = cc + c
                        if 0 <= rn < rows and 0 <= cn < cols:
                            sum_neighbors += g[rn][cn]
                neighbors[(rc, cc)] = sum_neighbors

        # Apply the game rules
        new_grid = np.zeros(shape=(rows, cols), dtype= int)
        for rc in range(rows):
            for cc in range(cols):
                if g[rc][cc] == 1 and neighbors[(rc, cc)] in [2, 3]:
                    new_grid[rc][cc] = 1
                elif g[rc][cc] == 0 and neighbors[(rc, cc)] == 3:
                    new_grid[rc][cc] = 1
                else:
                    new_grid[rc][cc] = 0
        self.life_grid = new_grid

    def make_n_steps(self, n):
        """
        Advance the simulation by multiple generations.
        
        Parameters:
        -----------
        n : input --> Enter the number of generations to simulate
        """
        for i in range(1,n + 1):
            # print(f'\nStep {i}\n') # Optional print progresseach step
            self.make_step()


    def _setup_axes(self, ax):
        """Private helper to configure axes appearance."""
        
        # Get current grid and dimensions
        g = self.life_grid
        x, y = self.cols, self.rows

        # Custom colormap: dark blue for dead, gold for alive
        colors = ["#11116CF9" , "#B3B314"]
        cmap = plt.cm.colors.ListedColormap(colors)

        # extent sets coordinates from 0 to dimensions for proper grid alignment
        self.im = ax.imshow(g, cmap=cmap, origin='upper', extent=[0, x, 0, y])

        # Add grid lines between cells
        ax.set_xticks(range(x), minor=True) 
        ax.set_yticks(range(y), minor=True)
        ax.grid(which="minor", color="black", linestyle='solid', linewidth=1)
        
        # Set proper boundaries and aspect ratio
        ax.set_xlim(0, x)
        ax.set_ylim(0, y)
        ax.set_aspect('equal')

        # Remove axis labels and ticks
        ax.tick_params(which="minor", size=0)
        ax.set_xticks([])
        ax.set_yticks([])

    def draw_grid(self, ax=None, fig=None):
        """
        Visualize the current grid state using matplotlib.
        
        Colors:
        -------
        Dead cells : #11116CF9 (dark blue)
        Live cells : #B3B314 (golden yellow)
        Grid lines : black
        """ 

        # Create or reuse figure
        if ax is None:
            fig, ax = plt.subplots(figsize=(6,6))

            self._setup_axes(ax)

            self.fig = fig
            self.ax = ax

            new_figure = True
        else:
            # UPDATE THE EXISTING IMAGE DATA
            self.im.set_data(self.life_grid)
            new_figure = False
     
        ax.set_title(f"Generation {self.current_step}")

        if new_figure:
            plt.tight_layout()
            plt.show()
        else:
            fig.canvas.draw()
            plt.pause(0.001)
        
        return ax, fig
    
    def animate(self, steps=20, delay=0.2):
        """Animate multiple generations in one window"""
        plt.ion()
        
        fig, ax = plt.subplots(figsize=(6,6))

        self._setup_axes(ax)
        
        # Animation loop
        for frame in range(steps):
            # JUST UPDATE DATA - no new objects!
            self.im.set_data(self.life_grid)

            ax.set_title(f"Generation {self.current_step}")
            
            fig.canvas.draw()
            plt.pause(delay)
            
            if frame < steps - 1:
                self.make_step()
        
        plt.ioff()
        plt.show()