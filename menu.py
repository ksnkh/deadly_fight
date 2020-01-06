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
        pass

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


control = {'ПРЫЖОК': 'W',
           'ПРИСЕСТЬ': 'S',
           'ВЛЕВО': 'A',
           'ВПРАВО': 'D',
           'УДАР': 'Y',
           'СИЛЬНЫЙ УДАР': 'U',
           'УДАР НОГОЙ': 'I',
           'СИЛЬНЫЙ УДАР НОГОЙ': 'O',
           'БЛОК': 'SPACE',
           'X-RAY': 'P'}


class Settings:
    def __init__(self, music_class, sound_class):
        self.points = [(30, 100, 'Музыка: вкл/выкл', (250, 250, 30), (250, 30, 250), 0),
                       (30, 200, 'Звуки: вкл/выкл', (250, 250, 30), (250, 30, 250), 1),
                       (30, 300, 'Назад', (250, 250, 30), (250, 30, 250), 2),
                       (450, 35, 'Управление', (250, 250, 30), (250, 30, 250), 3),
                       (350, 100, 'ПРЫЖОК', (250, 250, 30), (250, 30, 250), 3),
                       (350, 140, 'ПРИСЕСТЬ', (250, 250, 30), (250, 30, 250), 4),
                       (350, 180, 'ВЛЕВО', (250, 250, 30), (250, 30, 250), 5),
                       (350, 220, 'ВПРАВО', (250, 250, 30), (250, 30, 250), 6),
                       (350, 260, 'УДАР', (250, 250, 30), (250, 30, 250), 7),
                       (350, 300, 'СИЛ. УДАР', (250, 250, 30), (250, 30, 250), 8),
                       (350, 340, 'УДАР НОГОЙ', (250, 250, 30), (250, 30, 250), 9),
                       (350, 380, 'СИЛ. УДАР НОГОЙ', (250, 250, 30), (250, 30, 250), 10),
                       (350, 420, 'БЛОК', (250, 250, 30), (250, 30, 250), 11),
                       (350, 460, 'X-RAY', (250, 250, 30), (250, 30, 250), 12),
                       (700, 100, control['ПРЫЖОК'], (250, 250, 30), (250, 30, 250), 3),
                       (700, 140, control['ПРИСЕСТЬ'], (250, 250, 30), (250, 30, 250), 4),
                       (700, 180, control['ВЛЕВО'], (250, 250, 30), (250, 30, 250), 5),
                       (700, 220, control['ВПРАВО'], (250, 250, 30), (250, 30, 250), 6),
                       (700, 260, control['УДАР'], (250, 250, 30), (250, 30, 250), 7),
                       (700, 300, control['СИЛЬНЫЙ УДАР'], (250, 250, 30), (250, 30, 250), 8),
                       (700, 340, control['УДАР НОГОЙ'], (250, 250, 30), (250, 30, 250), 9),
                       (700, 380, control['СИЛЬНЫЙ УДАР НОГОЙ'], (250, 250, 30), (250, 30, 250), 10),
                       (700, 420, control['БЛОК'], (250, 250, 30), (250, 30, 250), 11),
                       (700, 460, control['X-RAY'], (250, 250, 30), (250, 30, 250), 12)]
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
            return 'main'
        # УПРАВЛЕНИЕ
        elif paragraph == 3:
            self.change('up_set')
        elif paragraph == 4:
            self.change('down_set')
        elif paragraph == 5:
            self.change('left_set')
        elif paragraph == 6:
            self.change('right_set')
        elif paragraph == 7:
            self.change('hit_set')
        elif paragraph == 8:
            self.change('power_hit_set')
        elif paragraph == 9:
            self.change('foot_set')
        elif paragraph == 10:
            self.change('power_foot_set')
        elif paragraph == 11:
            self.change('jump_set')
        elif paragraph == 12:
            self.change('xray_set')

    def change(self, set):
        if set == 'up_set':
            print(1)
        elif set == 'down_set':
            print('1')
        elif set == 'left_set':
            print('1')
        elif set == 'right_set':
            print('1')
        elif set == 'hit_set':
            print('1')
        elif set == 'power_hit_set':
            print('1')
        elif set == 'foot_set':
            print('1')
        elif set == 'rower_foot_set':
            print('1')
        elif set == 'jump_set':
            print('1')
        elif set == 'xray_set':
            print('1')

    def drawing(self, surface, font_menu, number_point):
        for i in self.points:
            if i != self.points[3]:
                if number_point == i[5]:
                    surface.blit(font_menu.render(i[2], 2, i[4]), (i[0], i[1]))
                else:
                    surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            else:
                if number_point == i[5]:
                    surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
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
                        paragraph = (paragraph - 1) % 13
                    if i.key == pygame.K_DOWN:
                        paragraph = (paragraph + 1) % 13
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