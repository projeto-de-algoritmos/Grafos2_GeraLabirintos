import pygame
from colors import BLACK, STANDARD_COLOR

# Classes
from Board import Board

pygame.init()

screen_size = (1600,800)
screen = pygame.display.set_mode(screen_size)
screen.fill(BLACK) # Set background color

# Screen title
pygame.display.set_caption("Gera Labirintos")

# Create an object to help track time
clock = pygame.time.Clock()

# Objects
board = Board(25, 25, 15, 15, 5, STANDARD_COLOR)