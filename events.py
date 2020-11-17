import sys


class Events:
    def __init__(self, pygame, player):
        self.__pygame = pygame
        self.__player = player

    def check_events(self):
        for event in self.__pygame.event.get():

            if event.type == self.__pygame.QUIT:
                self.__pygame.quit()
                sys.exit()

            # Keyup events
            if event.type == self.__pygame.KEYDOWN:
                if ((event.key == self.__pygame.K_a) or 
                (event.key == self.__pygame.K_LEFT)):
                    self.__player.move_left()

                elif ((event.key == self.__pygame.K_d) or 
                (event.key == self.__pygame.K_RIGHT)):
                    self.__player.move_right()
