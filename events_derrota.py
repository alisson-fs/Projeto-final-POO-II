import sys
import pygame
from events import Events
import sys

class EventsDerrota(Events):
    def __init__(self, textbox):
        self.__mouseClick = False
        self.__textbox = textbox

    @property
    def mouseClick(self):
        return self.__mouseClick

    @property
    def events(self):
        return pygame.event.get()

    def check_events(self):
        self.__mouseClick = False
        events = pygame.event.get()
        for event in events:

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__mouseClick = True
            else:
                self.__mouseClick = False

        self.__textbox.listen(events)
