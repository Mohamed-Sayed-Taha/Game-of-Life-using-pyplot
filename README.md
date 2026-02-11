# Game-of-Life-using-pyplot

# Game of Life

Conway's Game of Life implementation with Python, NumPy, and Matplotlib.

## Quick Start 🚀

```python
from game_of_life import GameOfLife

# Create 30x30 grid
game = GameOfLife(30, 30)

# Random start
game.randomize(density=0.2)

# Animate 50 generations
game.animate(steps=50, delay=0.1)



Features
Pure Python + NumPy

8 built-in patterns

Smooth animation

No memory leak



Installation
bash
pip install numpy matplotlib
pip install numpy Numpy



Author
Mohamed Sayed Taha


Usage Examples
Glider:

game = GameOfLife(20, 20)
game.populate_grid([(1,2), (2,3), (3,1), (3,2), (3,3)])
game.animate(steps=30, delay=0.2)
Random pattern:

game = GameOfLife(30, 30)
game.randomize(density=0.2)
game.animate(steps=50, delay=0.1)



Project Structure

game-of-life/
├── game_of_life.py    # Main class
├── patterns.py        # Pattern library
├── main.py           # Examples & demos
└── README.md         # You are here
