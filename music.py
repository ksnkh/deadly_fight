import pygame
from random import choice

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class Music:
    def __init__(self):
        a = choice([1, 2, 3])
        if a == 1:
            song = 'music\music.mp3'
        elif a == 2:
            song = 'music\гладиатор.mp3'
        else:
            song = 'music\комбат.mp3'
        self.on = True
        pygame.mixer.music.load(song)

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
