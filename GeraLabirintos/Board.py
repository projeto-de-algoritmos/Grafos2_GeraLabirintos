from pygame import draw, Surface
from colors import BLACK, WALL
from random import randint
import random

class Board():
    def __init__(self, width: int, height: int, horizontal: int, vertical: int, margin: int, standard_color: tuple) -> None:
        self.width = width
        self.height = height
        self.vertical = vertical
        self.horizontal = horizontal
        self.margin = margin
        self.color = standard_color
        # directions to walk
        self.dx = [ -1, 1, 0,  0]
        self.dy = [  0, 0, 1, -1]
        self.grid = [[standard_color for i in range(vertical)] for j in range(horizontal)]

    def out_of_range(self, x: int, y: int) -> bool:
        """tells if x or y access self.grid invalid position

                Parameters:
                        x (int): x position in grid
                        y (int): y position in grid

                Returns:
                        True (bool):  is out of range
                        False (bool): is in range
        """
        return (x < 0 or y < 0 or x >= self.horizontal or y >= self.vertical)

    def screen_to_grid(self, x: int, y: int) -> tuple:
        """Change the x/y screen coordinates to grid coordinates

                Parameters:
                        x (int): x screen coordinates
                        y (int): y screen coordinates

                Returns:
                        (x, y) (tuple): grid coordinates
        """
        return (y // (self.width + self.margin), x // (self.height + self.margin))

    def draw_grid(self, screen: Surface) -> None:
        """draw grid to specific screen

                Parameters:
                        screen (Surface): game screen

                Returns:
                        None
        """
        for row in range(self.horizontal):
            for column in range(self.vertical):
                draw.rect(screen,
                          self.grid[row][column],
                          [(self.margin + self.width) * (2 + column) + self.margin,
                          (self.margin + self.height) * (2 + row) + self.margin,
                          self.width,
                          self.height])

    def maze_prim(self, x: int, y: int, screen: Surface) -> None:
        """draw maze in the screen based on prim's algorithm

                Parameters:
                        x (int): x screen coordinates
                        y (int): y screen coordinates
                        screen (Surface): game screen

                Returns:
                        None
        """
        check = [[False for i in range(self.vertical)] for j in range(self.horizontal)]

        vetX = []
        vetY = []
        vetNX = []
        vetNY = []

        n = 0
        vetX.append(x)
        vetY.append(y)

        vetNX.append(0)
        vetNY.append(0)

        while vetX:

                n = randint(0, len(vetX) - 1)

                if self.out_of_range(vetX[n], vetY[n]) or check[vetX[n]][vetY[n]] == True:
                        vetX.pop(n)
                        vetY.pop(n)
                        vetNX.pop(n)
                        vetNY.pop(n)
                        continue

                draw.rect(screen, WALL,
                ((self.margin + self.width) * (2.35 + vetY[n]) + self.margin,
                 (self.margin + self.height) * (2.35 + vetX[n]) + self.margin,
                  13, 13))

                draw.rect(screen, WALL,
                ((self.margin + self.width) * (2.35 + vetY[n] + (vetNY[n] / 2)) + self.margin,
                 (self.margin + self.height) * (2.35 + vetX[n] + (vetNX[n] / 2)) + self.margin,
                  13, 13))

                check[vetX[n]][vetY[n]] = True
                
                for i in range(0, 4):
                        newX = vetX[n]+self.dx[i]
                        newY = vetY[n]+self.dy[i]
                        if not (self.out_of_range(newX, newY) or check[newX][newY] == True):
                                vetX.append(newX)
                                vetY.append(newY)
                                vetNX.append(self.dx[i])
                                vetNY.append(self.dy[i])