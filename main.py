"""
Game of Life - Examples and Demos
"""
from game_of_life import GameOfLife
from patterns import get_pattern, list_patterns

def demo_glider():
    """Glider pattern - moves diagonally"""
    game = GameOfLife(20, 20)
    game.populate_grid(get_pattern(1))
    game.animate(steps=30, delay=0.2)

def demo_pulsar():
    """Pulsar - oscillates every 3 generations"""
    game = GameOfLife(30, 30)
    game.populate_grid(get_pattern(8))
    game.animate(steps=20, delay=0.3)

def demo_random():
    """Random pattern"""
    game = GameOfLife(30, 30)
    game.randomize(density=0.2)
    game.animate(steps=50, delay=0.1)

def demo_r_pentomino():
    """R-pentomino - famous chaotic pattern"""
    game = GameOfLife(50, 50)
    r_pento = [(14,15), (15,15), (16,15), (15,14), (15,16)]
    game.populate_grid(r_pento)
    game.animate(steps=200, delay=0.05)

if __name__ == "__main__":
    list_patterns()
    demo_r_pentomino()