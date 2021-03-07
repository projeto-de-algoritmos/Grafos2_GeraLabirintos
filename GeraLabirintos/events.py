from pygame import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame import mouse
from buttonsHelper import buttons_on_click

def treats_event(event) -> bool:
    """treats pygame events

            Parameters:
                    event (Event): pygame event

            Returns:
                    True (bool): quit game
                    False (bool): stay playing
    """
    if event.type == QUIT:
        return True
    elif event.type == MOUSEBUTTONDOWN:
        x, y = mouse.get_pos()
        buttons_on_click(x, y)
    return False
