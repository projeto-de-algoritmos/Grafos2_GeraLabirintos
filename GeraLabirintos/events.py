from pygame import QUIT

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