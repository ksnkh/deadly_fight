import pygame

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

class Music:
    def __init__(self):
        self.on = True
        pygame.mixer.music.load('music\music.mp3')

    def play(self):
        pygame.mixer.music.play(-1)

    def not_play(self):
        pygame.mixer.music.pause()


#Флекс в доработке
class Music_Flex:
    def __init__(self):
        self.on = True
        pygame.mixer.music.load('flex.mp3')

    def play(self):
        pygame.mixer.music.play(-1)

    def not_play(self):
        pygame.mixer.music.pause()


class Sound:
    def __init__(self):
        self.on = True

    def play(self, file_name):
        sound1 = pygame.mixer.Sound(file_name)
        if self.on:
            sound1.play()
