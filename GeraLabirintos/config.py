import pygame
from colors import BLACK, STANDARD_COLOR, LIGHTBLUE, PRIM_COLOR

# Classes
from Board import Board
from Button import Button

pygame.init()

screen_size = (1600,800)
screen = pygame.display.set_mode(screen_size)
screen.fill(LIGHTBLUE) # Set background color

# Screen title
pygame.display.set_caption("Gera Labirintos")

# Create an object to help track time
clock = pygame.time.Clock()

# All buttons
maze_button = Button(PRIM_COLOR, 1315, 200, 225, 200, "Maze")
buttons = [maze_button]

# Objects
board = Board(25, 25, 40, 50, 0, STANDARD_COLOR)
