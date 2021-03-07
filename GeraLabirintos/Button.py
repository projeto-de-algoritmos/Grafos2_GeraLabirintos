import pygame

class Button():
    def __init__(self, color:tuple, x:int, y:int, width:int, height:int, text='') -> None:
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen) -> None:
        """draw the button on the screen
            Parameters:
                    screen (): main screen
        """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (255, 255, 255))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                self.y + (self.height/2 - text.get_height()/2)))

    def check(self, x:int, y:int) -> bool:
        """check if the mouse click the button
            Parameters:
                    x (int): x screen coordinate
                    y (int): y screen coordinate
            Returns:
                    True (bool): click on the button
                    False (bool): didn't click on the button
        """
        if x > self.x and x < self.x + self.width:
            if y > self.y and y < self.y + self.height:
                return True
            
        return False
