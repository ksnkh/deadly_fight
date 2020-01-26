import pygame
from moviepy.editor import *
from music import Music, Sound
from settings import Settings

pygame.init()
pygame.mixer.init()
size = width, height = 800, 500
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
                       [620, 100, 'C', (128, 128, 128), 3],
                       [620, 140, 'R', (128, 128, 128), 4],
                       [620, 180, 'E', (128, 128, 128), 5],
                       [620, 220, 'A', (128, 128, 128), 6],
                       [620, 260, 'T', (128, 128, 128), 7],
                       [620, 300, 'O', (128, 128, 128), 8],
                       [620, 340, 'R', (128, 128, 128), 9],
                       [620, 380, 'S', (128, 128, 128), 10]]
        pygame.time.wait(200)
        screen.fill(pygame.Color('black'))
        image_0 = pygame.image.load('other\обои_пепе1.png')
        screen.blit(image_0, (0, 0))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        pygame.display.flip()

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
                       [620, 100, 'C', (128, 128, 128), 3],
                       [620, 140, 'R', (128, 128, 128), 4],
                       [620, 180, 'E', (128, 128, 128), 5],
                       [620, 220, 'A', (128, 128, 128), 6],
                       [620, 260, 'T', (128, 128, 128), 7],
                       [620, 300, 'O', (128, 128, 128), 8],
                       [620, 340, 'R', (128, 128, 128), 9]]
        pygame.time.wait(200)
        screen.fill(pygame.Color('black'))
        image_0 = pygame.image.load('other\обои_пепе2.png')
        screen.blit(image_0, (0, 0))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        pygame.display.flip()

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
                       [620, 100, 'C', (128, 128, 128), 3],
                       [620, 140, 'R', (128, 128, 128), 4],
                       [620, 180, 'E', (128, 128, 128), 5],
                       [620, 220, 'A', (128, 128, 128), 6],
                       [620, 260, 'T', (128, 128, 128), 7],
                       [620, 300, 'O', (128, 128, 128), 8]]
        pygame.time.wait(200)
        screen.fill(pygame.Color('black'))
        image_0 = pygame.image.load('other\обои_пепе3.png')
        screen.blit(image_0, (0, 0))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        pygame.display.flip()

        self.points = [[30, 100, 'Музыка: вкл', (128, 128, 128), 0],
                       [30, 180, 'Звуки: вкл', (128, 128, 128), 1],
                       [30, 260, 'Назад', (128, 128, 128), 1],
                       [420, 35, 'Управление', (240, 240, 240), 3],
                       [350, 100, 'ВВЕРХ', (128, 128, 128), 3],
                       [350, 140, 'ВНИЗ', (128, 128, 128), 4],
                       [350, 180, 'ВЛЕВО', (128, 128, 128), 5],
                       [350, 220, 'ВПРАВО', (128, 128, 128), 6],
                       [350, 260, 'УДАР', (128, 128, 128), 7],
                       [620, 100, 'C', (128, 128, 128), 3],
                       [620, 140, 'R', (128, 128, 128), 4],
                       [620, 180, 'E', (128, 128, 128), 5],
                       [620, 220, 'A', (128, 128, 128), 6],
                       [620, 260, 'T', (128, 128, 128), 7]]
        pygame.time.wait(200)
        screen.fill(pygame.Color('black'))
        image_0 = pygame.image.load('other\обои_пепе4.png')
        screen.blit(image_0, (0, 0))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        pygame.display.flip()

        self.points = [[30, 100, 'Музыка: вкл', (128, 128, 128), 0],
                       [30, 180, 'Звуки: вкл', (128, 128, 128), 1],
                       [420, 35, 'Управление', (240, 240, 240), 3],
                       [350, 100, 'ВВЕРХ', (128, 128, 128), 3],
                       [350, 140, 'ВНИЗ', (128, 128, 128), 4],
                       [350, 180, 'ВЛЕВО', (128, 128, 128), 5],
                       [350, 220, 'ВПРАВО', (128, 128, 128), 6],
                       [620, 100, 'C', (128, 128, 128), 3],
                       [620, 140, 'R', (128, 128, 128), 4],
                       [620, 180, 'E', (128, 128, 128), 5],
                       [620, 220, 'A', (128, 128, 128), 6]]
        pygame.time.wait(200)
        screen.fill(pygame.Color('black'))
        image_0 = pygame.image.load('other\обои_пепе.png')
        screen.blit(image_0, (0, 0))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        pygame.display.flip()

        self.points = [[30, 100, 'Музыка: вкл', (128, 128, 128), 0],
                       [30, 180, 'Звуки: вкл', (128, 128, 128), 1],
                       [420, 35, 'Управление', (240, 240, 240), 3],
                       [350, 100, 'ВВЕРХ', (128, 128, 128), 3],
                       [350, 140, 'ВНИЗ', (128, 128, 128), 4],
                       [350, 180, 'ВЛЕВО', (128, 128, 128), 5],
                       [620, 100, 'C', (128, 128, 128), 3],
                       [620, 140, 'R', (128, 128, 128), 4],
                       [620, 180, 'E', (128, 128, 128), 5]]
        pygame.time.wait(200)
        screen.fill(pygame.Color('black'))
        image_0 = pygame.image.load('other\обои_пепе.png')
        screen.blit(image_0, (0, 0))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        pygame.display.flip()

        self.points = [[30, 100, 'Музыка: вкл', (128, 128, 128), 0],
                       [420, 35, 'Управление', (240, 240, 240), 3],
                       [350, 100, 'ВВЕРХ', (128, 128, 128), 3],
                       [350, 140, 'ВНИЗ', (128, 128, 128), 4],
                       [620, 100, 'C', (128, 128, 128), 3],
                       [620, 140, 'R', (128, 128, 128), 4]]
        pygame.time.wait(200)
        screen.fill(pygame.Color('black'))
        image_0 = pygame.image.load('other\обои_пепе.png')
        screen.blit(image_0, (0, 0))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        pygame.display.flip()

        self.points = [[30, 100, 'Музыка: вкл', (128, 128, 128), 0],
                       [420, 35, 'Управление', (240, 240, 240), 3],
                       [350, 100, 'ВВЕРХ', (128, 128, 128), 3],
                       [620, 100, 'C', (128, 128, 128), 3]]
        pygame.time.wait(200)
        screen.fill(pygame.Color('black'))
        image_0 = pygame.image.load('other\обои_пепе.png')
        screen.blit(image_0, (0, 0))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        pygame.display.flip()

        self.points = [[420, 35, 'Управление', (240, 240, 240), 3]]
        pygame.time.wait(200)
        screen.fill(pygame.Color('black'))
        image_0 = pygame.image.load('other\обои_пепе.png')
        screen.blit(image_0, (0, 0))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        pygame.display.flip()

        self.points = []

        pygame.time.wait(200)
        screen.fill(pygame.Color('black'))
        image_0 = pygame.image.load('other\обои_пепе.png')
        screen.blit(image_0, (0, 0))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        pygame.display.flip()

        pygame.time.wait(250)

        image_0 = pygame.image.load('other\обои_пепе.png')
        screen.blit(image_0, (0, 0))

        f2 = pygame.font.SysFont('mr_AfronikG', 38)
        text2 = f2.render("СОЗДАТЕЛИ", 0, (255, 255, 255))
        screen.blit(text2, (420, 35))
        pygame.display.flip()
        pygame.time.wait(350)

        image_0 = pygame.image.load('other\саша.png')
        screen.blit(image_0, (100, 130))
        text2 = f2.render("ПЛЮТ АЛЕКСАНДР", 0, (240, 240, 240))
        screen.blit(text2, (280, 150))
        pygame.display.flip()
        pygame.time.wait(450)

        image_0 = pygame.image.load('other\костя.png')
        screen.blit(image_0, (100, 277))
        text2 = f2.render("НАХАМКИН КоНСТАНТИН", 0, (240, 240, 240))
        screen.blit(text2, (280, 290))
        pygame.display.flip()
        pygame.time.wait(550)

        image_0 = pygame.image.load('other\егор.png')
        screen.blit(image_0, (100, 417))
        text2 = f2.render("МИШАЛКИН ЕГОР", 0, (240, 240, 240))
        screen.blit(text2, (280, 437))
        pygame.display.flip()

        pygame.time.wait(5000)
    def run(self):
        m = Music()
        s = Sound()
        m.not_play()
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
        return 'ricardo'


class Ricardo():
    def __init__(self):
        pass

    def run(self):
        self.clip = VideoFileClip("other\Flex.mp4")
        self.clip.preview(24)
        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event == pygame.QUIT:
                    sys.exit()
            run = False
        screen.fill(pygame.Color('black'))
        pygame.display.flip()
        m = Music()
        s = Sound()
        m.play()
        settingsC = Settings(m, s)
        return 'settings'
