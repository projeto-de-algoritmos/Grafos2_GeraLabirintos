# Libraries
import pygame
# Functions
from events import treats_event
# Global constants and variables
from config import screen, clock, board
done = False

board.draw_grid(screen)
board.maze_prim(1, 1, screen)

while not done:
    # Frame rate
    clock.tick(60)
    # Update screen
    pygame.display.flip()
    # Treats player interaction
    for event in pygame.event.get():
        done = treats_event(event)