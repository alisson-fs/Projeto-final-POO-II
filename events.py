import sys
import pygame
from abc import ABC


class Events(ABC):
    def check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
