import pygame
import pyglet, ctypes
import sys
import moviepy
from moviepy.editor import *

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

class Egg:
    def __init__(self, music_class):
        self.points = [[30, 100, 'Музыка: вкл', (128, 128, 128), 0],
                       [30, 180, 'Звуки: вкл', (128, 128, 128), 1],
                       [30, 260, 'Назад', (128, 128, 128), 1],
                       [420, 35, 'Управление', (240, 240, 240), 3],
                       [350, 100, 'ВВЕРХ', (128, 128, 128), 3],
                       [350, 140, 'ВНИЗ', (128, 128, 128), 4],
                       [350, 180, 'ВЛЕВО', (128, 128, 128), 5],
                       [350, 220, 'ВПРАВО', (128, 128, 128), 6],
                       [350, 260, 'УДАР', (128, 128, 128), 7],
                       [350, 300, 'СИЛ.УДАР', (128, 128, 128), 8],
                       [350, 340, 'УДАР НОГОЙ', (128, 128, 128), 9],
                       [350, 380, 'СИЛ.УДАР НОГОЙ', (128, 128, 128), 10],
                       [350, 420, 'ПРЫЖОК', (128, 128, 128), 11],
                       [620, 100, 'C', (128, 128, 128), 3],
                       [620, 140, 'R', (128, 128, 128), 4],
                       [620, 180, 'E', (128, 128, 128), 5],
                       [620, 220, 'A', (128, 128, 128), 6],
                       [620, 260, 'T', (128, 128, 128), 7],
                       [620, 300, 'O', (128, 128, 128), 8],
                       [620, 340, 'R', (128, 128, 128), 9],
                       [620, 380, 'S', (128, 128, 128), 10],
                       [620, 420, '3', (128, 128, 128), 11]]
        self.music_class = music_class

    def drawing(self, surface, font_menu):
        screen.fill(pygame.Color('black'))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            pygame.display.flip()

    def run(self):
        self.points = [[30, 100, 'Музыка: вкл', (128, 128, 128), 0],
                       [30, 180, 'Звуки: вкл', (128, 128, 128), 1],
                       [30, 260, 'Назад', (128, 128, 128), 1],
                       [420, 35, 'Управление', (240, 240, 240), 3],
                       [350, 100, 'ВВЕРХ', (128, 128, 128), 3],
                       [350, 140, 'ВНИЗ', (128, 128, 128), 4],
                       [350, 180, 'ВЛЕВО', (128, 128, 128), 5],
                       [350, 220, 'ВПРАВО', (128, 128, 128), 6],
                       [350, 260, 'УДАР', (128, 128, 128), 7],
                       [350, 300, 'СИЛ.УДАР', (128, 128, 128), 8],
                       [350, 340, 'УДАР НОГОЙ', (128, 128, 128), 9],
                       [350, 380, 'СИЛ.УДАР НОГОЙ', (128, 128, 128), 10],
                       [350, 420, 'ПРЫЖОК', (128, 128, 128), 11],
                       [620, 100, 'C', (128, 128, 128), 3],
                       [620, 140, 'R', (128, 128, 128), 4],
                       [620, 180, 'E', (128, 128, 128), 5],
                       [620, 220, 'A', (128, 128, 128), 6],
                       [620, 260, 'T', (128, 128, 128), 7],
                       [620, 300, 'O', (128, 128, 128), 8],
                       [620, 340, 'R', (128, 128, 128), 9],
                       [620, 380, 'S', (128, 128, 128), 10],
                       [620, 420, '3', (128, 128, 128), 11]]
        font = pygame.font.SysFont('mr_AfronikG', 38)
        self.drawing(screen, font)
        self.flex()
        pygame.time.wait(2050)
        return 'main'

    def flex(self):
        font = pygame.font.SysFont('mr_AfronikG', 38)
        #for i in range(13, 22):
        #    points = list(self.points[i][2])
        #    points[0] = '-'
        #    self.points[i][2] = ''.join(points)
        #    pygame.time.wait(250)
        #    self.drawing(screen, font)
        #for i in range(13, 21):
        #    sym = ['П', 'А', 'С', 'Х', 'А', 'Л', 'К', 'А']
        #   points = list(self.points[i][2])
        #    points[0] = sym[i - 13]
        #   self.points[i][2] = ''.join(points)
        #   pygame.time.wait(250)
        #    self.drawing(screen, font)
        clip = VideoFileClip("soon\Flex.mp4")
        clip.resize(width=100)
        run = True
        while run:
            clip.preview()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit(0)
            run = False
            screen.fill(0)
