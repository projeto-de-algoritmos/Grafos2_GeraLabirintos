from pygame import draw, Surface

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
        return (x < 0 or y < 0 or x >= self.width or y >= self.height)

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