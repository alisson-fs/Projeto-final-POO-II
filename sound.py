import pygame

class Sound:
    def __init__(self):
        #Inicializa sons
        # sound1 = pygame.mixer.music.load("Nivel1.mp3")
        

        #Lista com os sons
        self.sounds = []

        #Volume dos sons
        for sound in self.sounds:
            sound.set_volume(0.25)

        #Inicializa as musicas de fundo
        background_music = "Materials/background_sound.mp3"

        #Lista com as musicas de fundo
        self.musics = [background_music]

    #Toca um som da lista pelo index
    def playSound(self,index):
        pygame.mixer.Sound.play(self.sounds[index])

    #Toca uma musica
    def playMusic(self,index):
        pygame.mixer.music.load(self.musics[index])
        pygame.mixer.music.play(-1)

    #Para a musica atual
    def stopMusic(self):
        pygame.mixer.music.stop()
