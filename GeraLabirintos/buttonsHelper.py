from pygame import Surface
from Board import Board
from colors import STANDARD_COLOR, WALL, PRIM_COLOR, LIGHTBLUE
from config import screen, board, buttons

def buttons_on_click(x: int, y: int) -> None:
    """check if the mouse click the button
            Parameters:
                    x (int): x screen coordinate
                    y (int): y screen coordinate
    """
    for i in range(len(buttons)):
        if buttons[i].check(x,y):
                screen.fill(LIGHTBLUE)
                board.draw_grid(screen)
                if(buttons[i].color == PRIM_COLOR):
                        board.maze_prim(1, 1, screen)

def draw_buttons() -> None:
    """draw the buttons on the screen"""
    for i in range(len(buttons)):
        buttons[i].draw(screen)
