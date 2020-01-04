import pygame
import sys
import os

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

fall = 1
pygame.time.set_timer(fall, 10)
fps = 80
clock = pygame.time.Clock()

settings = {'music': 1, 'sound': 1}


class Music:
    def __init__(self):
        self.on = True
        pygame.mixer.music.load('music.mp3')

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


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


# В main_menu добавляются ф-ии меню, которые могут быть открыты
# Вместо game потом надо добавить select_character
class MainMenu:
    def __init__(self):
        self.points = [(30, 100, 'Подключиться к серверу', (250, 250, 30), (250, 30, 250), 0),
                       (30, 200, 'Создать сервер', (250, 250, 30), (250, 30, 250), 1),
                       (30, 300, 'Настройки', (250, 250, 30), (250, 30, 250), 2),
                       (30, 400, 'Выход', (250, 250, 30), (250, 30, 250), 3)]
        self.font = pygame.font.SysFont('serif', 30)
        self.called_menu = None

    def drawing(self, surface, font_menu, number_point):
        for i in self.points:
            if number_point == i[5]:
                surface.blit(font_menu.render(i[2], 2, i[4]), (i[0], i[1]))
            else:
                surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))

    def clicked(self, paragraph):
        if paragraph == 0:
            # В будующем надо будет вызывать меню подключения к серверу
            return 'connect to server'
        elif paragraph == 1:
            # В будующем надо будет вызывать меню выбора персонажа место начала игры
            return 'fight'
        elif paragraph == 2:
            return 'settings'
        elif paragraph == 3:
            sys.exit()

    def run(self):
        running = True
        paragraph = 0  # номер кнопки
        font = pygame.font.SysFont('serif', 30)
        while running:
            mouse = pygame.mouse.get_pos()
            for i in self.points:
                # меняем подсвечиваемую кнопку, при наведении на неё мышкой
                if mouse[0] > i[0] and mouse[0] < i[0] + 155 and mouse[1] > i[1] and mouse[1] < i[1] + 50:
                    paragraph = i[5]
            self.drawing(screen, font, paragraph)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    # меняем подсвечиваемую кнопку кнопками верх/вниз, если это возможно
                    if i.key == pygame.K_UP:
                        paragraph = (paragraph - 1) % 4
                    if i.key == pygame.K_DOWN:
                        paragraph = (paragraph + 1) % 4
                    # вызываем действия от подсвечиваемой кнопки при нажатии на enter
                    if i.key == 13:
                        called_menu = self.clicked(paragraph)
                        running = False
                # вызываем действия от подсвечиваемой кнопки при нажатии на левую кнопку мыши/enter
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    called_menu = self.clicked(paragraph)
                    running = False
            screen.blit(screen, (0, 0))
            pygame.display.flip()
        screen.fill(pygame.Color('black'))
        return called_menu


class Settings:
    def __init__(self, music_class, sound_class):
        self.points = [(30, 100, 'Музыка: вкл/выкл', (250, 250, 30), (250, 30, 250), 0),
                       (30, 200, 'Звуки: вкл/выкл', (250, 250, 30), (250, 30, 250), 1),
                       (30, 300, 'Управление', (250, 250, 30), (250, 30, 250), 2),
                       (30, 400, 'Назад', (250, 250, 30), (250, 30, 250), 3)]
        self.music_class = music_class
        self.sound_class = sound_class

    def clicked(self, paragraph):
        if paragraph == 0:
            if self.music_class.on:
                self.music_class.not_play()
                self.music_class.on = False
            else:
                self.music_class.play()
                self.music_class.on = True
        elif paragraph == 1:
            if self.sound_class.on:
                self.sound_class.on = False
            else:
                self.sound_class.on = True
        elif paragraph == 2:
            # В будующем надо будет сделать управление
            return 'control'
        elif paragraph == 3:
            return 'main'

    def drawing(self, surface, font_menu, number_point):
        for i in self.points:
            if number_point == i[5]:
                surface.blit(font_menu.render(i[2], 2, i[4]), (i[0], i[1]))
            else:
                surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))

    def run(self):
        font = pygame.font.SysFont('serif', 30)
        paragraph = 0  # номер кнопки
        running = True
        while running:
            mouse = pygame.mouse.get_pos()
            for i in self.points:
                # меняем подсвечиваемую кнопку, при наведении на неё мышкой
                if mouse[0] > i[0] and mouse[0] < i[0] + 155 and mouse[1] > i[1] and mouse[1] < i[1] + 50:
                    paragraph = i[5]
            self.drawing(screen, font, paragraph)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_UP:
                        paragraph = (paragraph - 1) % 4
                    if i.key == pygame.K_DOWN:
                        paragraph = (paragraph + 1) % 4
                    # вызываем действия от подсвечиваемой кнопки при нажатии на enter
                    if i.key == 13:
                        called_menu = self.clicked(paragraph)
                        running = False
                # вызываем действия от подсвечиваемой кнопки при нажатии на левую кнопку мыши/enter
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    called_menu = self.clicked(paragraph)
                    running = False
            screen.blit(screen, (0, 0))
            pygame.display.flip()
        screen.fill(pygame.Color('black'))
        return called_menu


class Fight:
    def run(self):
        print(1)
        return 'main'


def select_fighter():
    pass


m = Music()
s = Sound()
m.play()
mainC = MainMenu()
settingsC = Settings(m, s)
fightC = Fight()
current_menu = mainC
while True:
    t = current_menu.run()
    if t == 'settings':
        current_menu = settingsC
    elif t == 'main':
        current_menu = mainC
    elif t == 'fight':
        current_menu = fightC
