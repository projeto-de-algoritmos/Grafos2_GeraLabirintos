# Libraries
import pygame
# Functions
from events import treats_event
from buttonsHelper import draw_buttons
# Global constants and variables
from config import screen, clock, buttons, board

board.draw_grid(screen)

done = False
while not done:
    draw_buttons()
    # Frame rate
    clock.tick(60)
    # Update screen
    pygame.display.flip()
    # Treats player interaction
    for event in pygame.event.get():
        done = treats_event(event)
