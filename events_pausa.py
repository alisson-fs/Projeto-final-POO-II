import pygame
from events import Events

class EventsPausa(Events):
    def __init__(self):
        self.__pausa = False

    @property
    def pausa(self):
        return self.__pausa

    @pausa.setter
    def pausa(self, pausa):
        self.__pausa = pausa

    def check_events(self):
        self.__pausa = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Keyup events
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_p):
                    self.__pausa = True
