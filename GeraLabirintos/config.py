import pygame
from colors import BLACK, STANDARD_COLOR, LIGHTBLUE

# Classes
from Board import Board

pygame.init()

screen_size = (1600,800)
screen = pygame.display.set_mode(screen_size)
screen.fill(LIGHTBLUE) # Set background color

# Screen title
pygame.display.set_caption("Gera Labirintos")

# Create an object to help track time
clock = pygame.time.Clock()

# Objects
board = Board(25, 25, 28, 50, 0, STANDARD_COLOR)